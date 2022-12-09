# demonstration of template string functions

from string import Template

def main():
    # usual string formatting with format() function
    str1 = "You're watching {0} by {1}".format("Advanced Python", "Joe Marini")
    print(str1)

    # eg 2
    templ = Template("You're watching ${title} by ${author}")
    str2 = templ.substitute(title="Advanced Python", author="Joe Marini")
    print(str2)

    # eg 3
    data = {
            "author": "Joe Marini",
            "title": "Advanced Python"
    }

    str3 = templ.substitute(data)
    print(str3)


if __name__ == "__main__":
    main()
