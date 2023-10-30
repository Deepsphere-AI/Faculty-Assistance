import os
import openai

def PythonEvaluator(functionality,code):
  response = openai.ChatCompletion.create(
    model=os.environ["MODEL"],
    messages=[
      {
        "role": "user",
        "content": f"""You will be provided with a piece of Python code for particular function , and carefully evaluate the code out of 10.If there's any indentation or syntax error the marks will be 0. Also, mention proper reason for why the mark is given.

          \n\n```
          Function : Reverse a Number\n
          \n# Reverse a Number\ndef reverse():\n\n    num = 1234\n    reversed_n = 0\n\n    while num != 0:\n        digit = num % 10\n        reversed_num = reversed_num * 10 + digit\n        num //= 10\n\n    print(\"Reversed Number: \" + str(reversed_num))\n\nreverse()\n\n```\n
          Marks out of 10: 8\n
          Reason for marks: The code provided is quite neat, logically correct, and gives the expected output of reversing the given number. It uses the approach of repetitively extracting the last digit of the number and appending it to the reversed number.\n\nHowever, two points are deducted for the following reasons:\n\n1. The variable initialized as 'reversed_n' should be 'reversed_num' to match its usage in the rest of the code. This is a simple typo but it will cause a NameError when the function is called.\n\n2. The number to be reversed is hard-coded in the function. It would have been better to make the number a parameter of the function so that any number could be reversed, increasing the function's flexibility and usability. For this reason, the function as it stands is not as versatile or robust as it could be.

          \n\n```
          Function : Reverse a Number\n
          \n# Reverse a Number\ndef reverse():\n\n   num = 1234\n    reversed_n = 0\n\n    while num != 0:\n        digit = num % 10\n        reversed_num = reversed_num * 10 + digit\n        num //= 10\n\n    print(\"Reversed Number: \" + str(reversed_num))\n\nreverse()\n\n```\n
          Marks out of 10: 0\n
          Reason for marks: The code provided has indentation error on the line where the variable "reversed_n" is declared. Python relies on indentation to define the scope in the code. Each code block (classes, functions, if statements, loops, etc.) starts with indentation and ends with the first unindented line. Besides, the "reversed_n" variable is initialized but never used later in the code. Instead, the code attempts to use "reversed_num" which was never defined, causing an error. Thus, the code wouldn't run correctly.

          \n\n```\n
          Function : {functionality}\n
          {code}
        \n```
        Marks out of 10:
        Reason for marks:
        """
      }
    ],
    temperature=0,
    max_tokens=300,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )
  return response["choices"][0]["message"]["content"]


def DescriptiveAnswerEval(a,b):
  response = openai.ChatCompletion.create(
    model=os.environ["MODEL"],
    messages=[
      {
        "role": "user",
        "content": f"""You're an descriptive type question answering system evaluator.
        For given actual answer and student provided answer, your responsiblity is to evaluate how similar the answers are without changing the context.
        Rate your evaluation out of 10 with proper reason.
        \n\nActual Answer:\n```\nA distributed system is a system whose components are located on different networked computers, which communicate and coordinate their actions by passing messages to one another. Distributed computing is a field of computer science that studies distributed systems.\n```
        \n\nStudent Answer:\n```\nDistributed computing is the method of making multiple computers work together to solve a common problem. It makes a computer network appear as a powerful single computer that provides large-scale resources to deal with complex challenges.\n```
        \n\nMarks out of 10: 8.5 out of 10\n
        Reason for marks: The student's answer captures the main idea of a distributed system, explaining that it's about networked computers that solve problems together, appearing as a powerful single computer. The answer could have been improved by stating specifically that these computers communicate and coordinate through the passing of messages like mentioned in the actual answer. The student also missed the point that distributed computing is a field of computer science that studies these systems.\n
        \n\nActual Answer:\n```\nMRO is a concept used in inheritance. It is the order in which a method is searched for in a classes hierarchy and is especially useful in Python because Python supports multiple inheritance. In Python, the MRO is from bottom to top and left to right.\n```
        \n\nStudent Answer:\n```\nSAP for Aerospace & Defense (SAP for A&D) provides a proven end-to-end MRO solution that supports processes for base maintenance, component repair, and line maintenance.\n```
        \n\nMarks out of 10: 2 out of 10\n,
        Reason for marks: The student's answer seems to be completely off the main topic. It has misunderstood MRO from Python programming context as Maintenance, Repair, and Overhaul in Aerospace & Defense industry. Therefore, it does not explain the method resolution order in inheritance concept in Python, as required in the actual answer. It seriously deviates from the original context and does not deliver any needed information about MRO in Python.
        \n\nActual Answer:\n```\n{a}```
        \n\nStudent Answer:\n```\n{b}```
        Marks out of 10:\n
        Reason for marks:
        """
      }
    ],
    temperature=0,
    max_tokens=350,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )
  return response["choices"][0]["message"]["content"]