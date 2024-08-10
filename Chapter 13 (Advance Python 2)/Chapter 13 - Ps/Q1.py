#1. Create two virtual environments, install few packages in the first one. How do you create a similar environment in the second one?


                                                    # ALL ARE DONE IN TERMINAL
# I created two environments env1 and env2 . then i install pandas and pyjokes in env1 and after deactivate and then activate env2 and add 


# step 1 - open terminal write - virtualenv env1
# step 2 - open terminal write - virtualenv env2

# FOR ACTIVATE ENV1 - .\env1\Scripts\activate.ps1

# for installing  modules - pip install pandas and pyjokes
    
# for generating requirements files - pip freeze > requirements.txt
    
#                 deactivate env1.
    
# then activate env2 - .\env2\Scripts\activate.ps1
# then adding requirements or similar environments as env1 - pip install -r .\requirements.txt

# after that all modules are install in env2.
