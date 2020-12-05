# Employee Database
This repo is a GraphQL implementation of a single table (employees) using Flask and Graphene. The app has authentication (JWT) and exposes the web based graphiQL editor too. Qxf2 uses this app to practice writing tests, learning to make graphQL queries and as a starting point to understanding the relationship between schemas and the exposed queries.

### Setup

0. Clone this repo
1. Setup a virtual environment (Python 3.7 or higher) and activate it `virtualenv -p python3.8 venv-employee-database`
2. `pip install -r requirements.txt`
3. Setup some fake data with `sqlite3 data/employee_database.sqlite3`
    > .mode csv
    > .import data/dummy_data.csv employee
    > select * from employee;
    > #You should see a couple of rows
    > .quit
4. Update `employees/secret.py` with any secret string you want to use
5. Start your server with `python run.py`

### Usage

1. Visit `http://localhost:5000/graphql` in your browser
2. Try the following query:
    ```
    mutation {
        auth(password: "clueless2!", username: "clueless") {
            accessToken
            refreshToken
            }
    }
    ```
3. If all goes well, step 2 will return an acessToken in the field - copy it
4. Use a browser plugin to modify your header. Add a `Authorization` key and set it to `Bearer accessToken` where `accessToken` is the token you copied in step 3.
5. Now try the 3 different queries allowed:

5a. Query all the employees

    ```
    query findAllEmployees{
        allEmployees{
            edges{
                node{
                    email
                    employeeId
                    dateJoined
                    isActive
                    blogAuthorName
                }
            }
        }
    }

    ```

5b. Query by employee email

    ```
    query FindEmployeeByEmail($email: String = "lasker@qxf2.com") {
        findEmployee(email: $email) {
            githubId
                blogAuthorName
                phone
                skypeId
        }

    }
    ```

5c. Query by employee Skype id

    ```
    query FindEmployeeBySkype($skype_id: String = "emmanuel.lasker.qxf2") {
        findEmployee(skypeId: $skype_id) {
            email
                blogAuthorName
                phone
        }
    }
    ```

6. If all goes well, you should be seeing data returned. The dummy database currently has two employees populated - WIlhelm Steinitz and Emmanuel Lasker.