
import hashlib as _hashlib
from global_variables import GlobalVariables


def _define_credentials():
    return GlobalVariables.Credentials


def _gen_hash_sha256(key):
    sha = _hashlib.sha256()
    sha.update(key.encode('utf-8'))
    return sha.hexdigest()


def _is_log_on(login, passwd):
    _is_login_ok = False
    _is_pass_ok = False

    hash_login = _gen_hash_sha256(login)
    hash_passwd = _gen_hash_sha256(passwd)

    hashes = _define_credentials()

    if not hashes:
        print("Danger! Credentials are read from external file pass_hash_sha256.txt")
        with open(GlobalVariables.Hash_list_file) as hash_list_file:
            hashes = hash_list_file.readlines()

        hash_list_file.close()

    for _hash in hashes:
        if hash_login == _hash:
            _is_login_ok = True
        if hash_passwd == _hash:
            _is_pass_ok = True

    return _is_login_ok & _is_pass_ok
