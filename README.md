# activation_tracker

This is a lightweight backend service to monitor merchants' activation workflows, ensuring seamless onboarding and status tracking.

# Project Set up

1. Create virtual environment(env)\
   ` python -m venv env`
2. Activate the virtual environment\
   On MacOS/Linus\
   ` . env/bin/activate`\
   On Windows\
   `env\Scripts\activate`
3. Install project requirements\
   `pip install -r requirements.txt`

4. Start application\
   `python manage.py runserver`

5. Make migrations\
   `python manage.py migrate`


# API endpoints

| Actions                                                  | Method    | Route                 |
| -------------------------------------------------------- | --------- | --------------------- |
| Retrieves all merchants  onboarding details              | GET       | `/merchant/`          |
| Update merchants onboarding status                       | PUT       | `/merchant/{id}`      |
| Fetch merchant by merchant ID                            | GET       | `/merchant/{id}`      |
| Retrieves all merchant requirements                      | GET       | `/requirement/`       |
| Update merchant requirement records                      | PUT       | `/requirement/{id}`   |
| Retrieves requirement by merchant ID                     | GET       | `/requirement/{id}`   |

