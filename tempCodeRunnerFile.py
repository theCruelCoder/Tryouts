mypath = 'JAVA_HOME=/usr/bin'
env_name, _, env_path = mypath.partition("=")
print(env_name, env_path)