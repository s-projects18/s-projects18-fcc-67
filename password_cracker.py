import hashlib

def get_list(path):
  """import file and return ist as a list"""
  try:
    file_handle = open(path, 'r')
    l = file_handle.read().splitlines(0)
    file_handle.close()
    return l
  except:
    print("Error: Can't open file: ", path)  
    exit()

def check_hash(pw, hash):
  """create sha1-hash of pw and compare it with hash"""
  h = hashlib.new("sha1") # hash-generator
  h.update(pw.encode('ascii'))
  hashed = h.hexdigest()
  if hash==hashed:
    return True  
  return False

def crack_sha1_hash(hash, use_salts=False):
  """hash: SHA-1 hash of a password

  return the password if it is one of the top 10,000 passwords used"""  
  pathPw    = 'top-10000-passwords.txt'
  pathSalts = 'known-salts.txt'

  # read complete salt-list
  if use_salts==True:
    salts = get_list(pathSalts)

  # read complete password-list
  # (using a handle and iterating over it
  # leads to memory-warnings in repl.it)
  passwords = get_list(pathPw)

  # check paswords
  for pw in passwords:
    if use_salts:
      pw_var = []
      # NOT: salt + pw + salt
      for salt in salts:
        pw_var.append(pw + salt)
        pw_var.append(salt + pw)
      for pws in pw_var:  
        if check_hash(pws, hash)==True:
          return pw
    else:
      if check_hash(pw, hash)==True:
        return pw

  return "PASSWORD NOT IN DATABASE"

