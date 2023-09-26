from getpass import getpass
from fabric import Connection, SerialGroup, ThreadingGroup
import re

def main():
    with Connection("localhost") as con:
        con.local("hostname", replace_env=False)

    password = getpass("Please enter AlexandreRaspaud@10.188.102.220's password:\n")
    result = Connection(
        "alexandre@localhost",
        connect_kwargs={
            "password": password,
        }
    ).run("uname -s")
    with Connection("alexandre@localhost", connect_kwargs={"password": password}) as connection:
        output = connection.run("pwd")
        print(output.stdout)
        # connection.run("ifconfig")
        connection.run(f"/usr/bin/python3.10 {output.stdout.rstrip()}/VSCode/formation_python/sysadmin-python/test_file.py --arg1 lghgrh --arg2 kjgheug")
        output = connection.run(f"cat {output.stdout.rstrip()}/Hello.postman_collection.json | grep POST")
        # print(output.stdout.rstrip())
        # regex = re.compile("(.*POST.*)\n", re.MULTILINE)
        # print(regex.findall(output.stdout.rstrip()))
    # connection = Connection(
    #     "alexandre@localhost",
    #     connect_kwargs={
    #         "password": password,
    #     }
    # )
    # print(connection)
    # connection.run("ifconfig")

if __name__ == "__main__":
    main()