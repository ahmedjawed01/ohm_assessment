# README #
1. This is a sample application with basic functionality for the purposes of assessing technical candidates only.
2. Do not be overly concerned if there is code in this application which does not appear to do anything or is imperfect. Just focus on the task below.
3. Usually it takes about 2 hours in total on installation and these tasks. To respect your time, we don't ask that you spend more than this, and it is ok if you do not get to everything.
4. Write your code as if you were a team member working on a joint codebase with other developers and follow good team-based development practices.  Assume your fellow teammates have not seen the project requirements.  
5. Assume you are writing this code for a production environment where errors and edge-cases should be handled gracefully.  
6. This technical assessment is testing your *full-stack* abilities, consider the setup of the environment as part of the assessment.
7. Feel free to use Google and StackOverflow, after all, that is what we do in real-life programming.
8. However there are other pull requests in this repository, but please do not look at them and instead do your own work. Be aware that some of these pull requests have been planted there to check for cheating.   

### Setup ###
1. Setup for a new python project as normal, we recommend using virtualenv and python 3.6
    * For more details, follow: http://timsherratt.org/digital-heritage-handbook/docs/python-pip-virtualenv/
2. Setup a MySQL database (MySql 8)
3. *Fork* the [ohm_assessment](https://github.com/ohmconnect/ohm_assessment) repository into your own repo
4. Set your python path, eg `export PYTHONPATH=/path/to/my/repo`
5. Add the pip modules: `pip install -r requirements.txt`
6. Copy config/my_development.cnf.sample to config/my_development.cnf and update with your MySQL information
7. Create your MySQL database (use db name found in sample config file)
8. Add to your environment: `FLASK_ENVIRONMENT=development`
9. Import the seed.sql file into the database
10. Migrate to the latest version of the database with `alembic upgrade head`.
10. Create testing environment: create config/my_test.cnf as of config/my_development.cnf, setup a test db (using naming convention of development db but that clearly indicates this is your test db), import seed.sql, update new db:`FLASK_ENVIRONMENT=test alembic upgrade head`
11. Do not commit either of your config files to the git repo.
12. Push your changes. Note this should be on your *forked* repo, either on a master branch or any other branch. It should *not* be on the ohm_assessment repo.
13. Open a pull request from your_repo/ohm_assessment/your_branch to ohmconnect/ohm_assessment/master. 

### Checkpoint ###
1. Before proceeding further, ensure that you can:
    * see 3 rows in the user table in your database
    * Start the app with `python app_test.py`
    * The page at /dashboard is now visible and welcomes you to the task. This page will automatically log you in as user 1.
    * You can run unit tests with `py.test tests` and see 2 tests passing.

## Your Tasks ##
1. In the top right corner of the page, you can see the user's status level and name.  Change these to be the user's current number of points and email address.
    * Instead of "Status Level: <status_level> Chuck Norris", it should show the "Points: <points_value> <user_email>""

2. Write a migration to do the following:
    * Increase the point_balance for user 1 to 5000
    * Add a location for user 2, assuming they live in the USA
    * Change the tier for user 3 to Silver

3. Add a new route at /community
    * Add this as a dropdown option in the top right corner of the page, below "Dashboard"
    * List the 5 most recent users (most recently signed up user first), with columns for user's display_name, tier, and point_balance.
    * Assume we want this page to be fast, so use a raw MySQL query rather than any built-in ORM methods and consider what else can be done to increase page performance. 
    * This table of users should be bordered and striped (ie alternate rows and with grey and white stripes)
    * Your new page likely shares some styles with the dashboard. Ensure that these styles are located in a reasonable location and without duplication.
    
    * OPTIONAL: Display user phone numbers in an additional column. If users have multiple phone numbers, Some users may have more than 1 phone number, each phone number should be displayed on a separate line.
    
4. Refactor the User.is_below_tier method

5. Testing
    * Add any unit tests that you think would be valuable. Feel free to expand existing unit tests provided in the assessment if you think they are insufficient.

6. Refer to the steps in "Setup" to fork and open a pull request. Note that your proficiency with Git is part of the assessment.
    * Do not be concerned if your pull request is DECLINED. We do this routinely as part of assessment for all candidates.

** BONUS: If you have not yet spent much more than two hours on this assignment, add an additional feature of your own design!
For example, what other information might be useful to see? Be creative!

## Assessment Criteria ##
1. Ability to handle ambiguous requirements.
2. Python ability
3. MySQL
4. CSS and Javascript
5. Tests 
6. Development practices / code organization / development tools (eg git)

## Notes for Assessor ##
Checklist and process described in [Confluence](https://ohmconnect.atlassian.net/wiki/spaces/OH/pages/28737540/Programming+Test) - restricted access.
