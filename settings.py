
import xml.etree.ElementTree as ElementTree
from global_variables import GlobalVariables


# ----------------------------------------------------- Constants ---------------------------------------------------- #


# general tags
TAG_TITLE = "title"
TAG_DESCRIPTION = "description"

TAG_LIST_GENERAL = [
    TAG_TITLE,
    TAG_DESCRIPTION
]

# settings types
TAG_SETTINGS_TYPE_DEFAULT = "settings_type_default"
TAG_SETTINGS_TYPE_RECENT = "settings_type_recent"
TAG_SETTINGS_TYPE_SAVED = "settings_type_saved"

TAG_LIST_SETTINGS_TYPE = [
    TAG_SETTINGS_TYPE_DEFAULT,
    TAG_SETTINGS_TYPE_RECENT,
    TAG_SETTINGS_TYPE_SAVED
]

# settings
TAG_NAME = "name"
TAG_PROJECT_SETTINGS = "project_settings"
TAG_PICTURE_SETTINGS = "picture_settings"

TAG_LIST_SETTINGS = [
    TAG_NAME,
    TAG_PROJECT_SETTINGS,
    TAG_PICTURE_SETTINGS
]

# project settings
TAG_PROJECT_PATH = "project_path"
"""..."""

TAG_LIST_PROJECT_SETTINGS = [
    TAG_PROJECT_PATH
]

# settings picture settings
    #pre
TAG_PICTURE_SETTINGS_cfg_is_dim = "cfg_is_dim"
TAG_PICTURE_SETTINGS_cfg_dim_x1 = "cfg_dim_x1"
TAG_PICTURE_SETTINGS_cfg_dim_x2 = "cfg_dim_x2"
TAG_PICTURE_SETTINGS_cfg_dim_y1 = "cfg_dim_y1"
TAG_PICTURE_SETTINGS_cfg_dim_y2 = "cfg_dim_y2"
TAG_PICTURE_SETTINGS_cfg_contrast = "contrast"          # kontrast
TAG_PICTURE_SETTINGS_cfg_brightness = "brightness"      # jasnosc
TAG_PICTURE_SETTINGS_cfg_blur = "blur"                  # rozmycie
    #parse
TAG_PICTURE_SETTINGS_cfg_num_of_colours = "num_of_colours"
TAG_PICTURE_SETTINGS_cfg_colour_separation = "colour_separation"
    #post
TAG_PICTURE_SETTINGS_cfg_is_margin = "is_margin"
TAG_PICTURE_SETTINGS_cfg_margin_size = "margin_size"

TAG_LIST_PICTURE_SETTINGS = [
    TAG_PICTURE_SETTINGS_cfg_is_dim,
    TAG_PICTURE_SETTINGS_cfg_dim_x1,
    TAG_PICTURE_SETTINGS_cfg_dim_x2,
    TAG_PICTURE_SETTINGS_cfg_dim_y1,
    TAG_PICTURE_SETTINGS_cfg_dim_y2,
    TAG_PICTURE_SETTINGS_cfg_contrast,
    TAG_PICTURE_SETTINGS_cfg_brightness,
    TAG_PICTURE_SETTINGS_cfg_blur,
    TAG_PICTURE_SETTINGS_cfg_num_of_colours,
    TAG_PICTURE_SETTINGS_cfg_colour_separation,
    TAG_PICTURE_SETTINGS_cfg_is_margin,
    TAG_PICTURE_SETTINGS_cfg_margin_size
]

# allowed tag list
ALLOWED_TAGS = TAG_LIST_GENERAL \
               + TAG_LIST_SETTINGS_TYPE \
               + TAG_LIST_SETTINGS \
               + TAG_LIST_PROJECT_SETTINGS \
               + TAG_LIST_PICTURE_SETTINGS


# ------------------------------------------ Parse .xml file ----------------------------------------- #


def extract_settings(file_path):
    test_results = []
    try:
        is_ok = True
        tree = ElementTree.parse(file_path)
        root = tree.getroot()

        for test_unit in root.findall(TAG_TEST_UNIT):
            ans = parse_vt_test_results_branch(test_results_branch=test_unit)
            is_ok &= ans[0]
            test_results.extend(ans[1])

    except IOError:
        is_ok = False

    return is_ok, test_results


def parse_vt_test_results_branch(test_results_branch):
    is_ok = True
    test_cases_results = []
    for element in test_results_branch:
        # test case
        if element.tag in TAGS_TEST_CASES:
            ans1 = extract_vt_test_case_result(test_case_branch=element)
            if ans1[0]:
                test_cases_results.append(ans1[1])
            else:
                is_ok = False
        # test case list
        elif element.tag in TAGS_TEST_CASES_LIST:
            ans2 = extract_vt_test_case_list_result(test_case_branch=element)
            if ans2[0]:
                test_cases_results.append(ans2[1])
            else:
                is_ok = False
        # unknown tag
        elif element.tag not in ALLOWED_TAGS:
            is_ok = False
            #report_error_unknown_tag(reporter=parse_vt_test_results_branch, tag=element.tag)
    return is_ok, test_cases_results


def extract_vt_test_case_list_result(test_case_branch):
    """
    Function extracts results data from test case list.

    :param test_case_branch: element tree branch (xml lib)
        Branch of xml element test results tree.

    :return: tuple
        :parameter is_ok: bool
            - True - function executed successfully
            - False - error occurred function execution
        :parameter test_case_list: None or object of VTTestCaseResult class
            Results data of test case list.
    """
    tag = test_case_branch.tag
    title = get_title(branch=test_case_branch)
    description = get_description(branch=test_case_branch)
    # get children
    is_ok, children = parse_vt_test_results_branch(test_results_branch=test_case_branch)
    if is_ok:
        test_case_list = VTTestCaseResult(tag=tag, title=title, description=description, test_case_id=None, children=children)
    else:
        test_case_list = None
        _problem = "Error occured dureing children results extraction. Test case data:\nTag = %s\nTitle = %s\n" \
                   "Description = '%s'" % (tag, title, description)
        #report_error_data_not_found(reporter=extract_vt_test_case_list_result, more_info=_problem)
    return is_ok, test_case_list


# ------------------------------------------ getters ----------------------------------------- #


def get_project_path(branch):
    project_path = branch.find(TAG_PROJECT_PATH)
    if project_path is not None:
        project_path = project_path.text
    return project_path


