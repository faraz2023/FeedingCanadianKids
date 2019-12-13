# iteration-03.final.md

## Iteration XX

 * Start date: November 25, 2019
 * End date: December 1, 2019



## MVP v.s. Initial Product Documentation

In the `product and planning` document we identified 3 major target users and 12 user stories for our MVP. In the following lines we will overview how each of these target user groups can interact with our application, and we examine whether we have satisfied the acceptance criteria for our user stories.

### Target Users:
1. **Program Partners**: as expected, potential program partners can now access our deployed product, sign-up, and apply to become a program partner. If partnership is granted by the admins, the program partners can login into their accounts, make different change requests to admins, and they can also access and review their schedule. In addition, they can use our portal to make requests for delivery dates and the amount of delivery they need. 

2. **Restaurant Partners**: as expected, potential program partners can now access our deployed product, sign-up, and apply to become a program partner. If partnership is granted by the admins, the program partners can login into their accounts, make different change requests to admins, and they can also access and review their schedule. In addition, they can use our portal to make indications of the dates they are available and the amount of food they can provide. 

3. **Feeding Canadian Kids Admins**: As expected, admins can access our deployed product and login into their accounts. Admins can create new admins from their profile. Admins can go through applications, accept them or deny them. Admins can add, or remove pairings. They can also access end user profiles and review their requests.

    + Additions: 
        + We have added the ability for admins to provide comments when they reject an application and change information on an application when they are accepting it.
        + We have created a live notification system that allows the admins to keep track of the changes in the application environment and review information about new events (i.e. new applications, requests, sign ups). 



### User Stories: 

Here we review each of our user stories and in section *acceptance review* we will contrast the criteria with current implementation.

1. As a *potential Restaurant Partner* , I want to be able to access a sign-up page, so I can provide a summary and contact information for Feeding Canadian Kids admins to contact me.

    + Acceptance Criteria:
        + Potential Restaurant Partner can access a sign-up page
        + Potential Restaurant Partner can supply Feeding Canadian Kids admins with summary and information
        + Potential Restaurant Partner receives an email when they submit an application
    + Acceptance Review:
        + All three criteria has been met. Sign-up page can be accessed, potential users can provide admins with summery and contact information, and an email is sent to the admin email address and the user email address upon each sign-up.

2. As a *potential program partner*, I want to be able to access a sign-up page, so I can provide a summary and contact information for Feeding Canadian Kids admins to contact me.

    + Acceptance Criteria:
        + Potential program partner can access a sign-up page
        + Potential program partner can supply Feeding Canadian Kids admins with summary and information
        + Potential program partner receives an email when they submit an application
    + Acceptance Review:
        + All three criteria has been met. Sign-up page can be accessed, potential users can provide admins with summery and contact information, and an email is sent to the admin email address and the user email address upon each sign-up.

3. As a *Restaurant Partner*, I want to be able to sign-in into my account so I will be able to see my donation schedule and to submit requests to Feeding Canadian Kids admins.

    + Acceptance Criteria:
        + Restaurant Partner can access a sign-in page(authentication with email and password)
        + Restaurant Partner can access a personal profile that shows basic statistics of their partnership with Feeding Canadian Kids
        + Restaurant Partners can submit a form in which they can request from Feeding Canadian Kids admins to:
            + Amend the donation schedule
            + Change the information on their account
    + Acceptance Review:
        + All three of the criteria has been met. Restaurant partners can sign-in, they can access a profile page and they can submit requests to admins in order to change their arrangements with Feeding Canadian Kids. 

4. As a *restaurant partner*, I want to have access to a resources page so I can learn who to use Feeding Canadian Kids application.

    + Acceptance Criteria:
        + Accessing a resources webpage through the restaurant partner profile
    + Acceptance Review:
        + The resources page has been created and restaurant partners can access it to review the resources made available to them by the admins.

5. As a *program partner*, I want to be able to sign-in into my account so I will be able to see my donation schedule and to submit requests to Feeding Canadian Kids admins.

    + Acceptance Criteria:
        + Program Partner can access a sign-in page (authentication with email and password)
        + Program Partner can access a personal profile that shows basic statistics of their partnership with Feeding Canadian Kids
        + Program Partner can submit a form in which they can request from Feeding Canadian Kids admins to:
            + Amend the food intake schedule
            + Change the information on their account
    + Acceptance Review:
        + All three of the criteria has been met. Program partners can sign-in, they can access a profile page and they can submit requests to admins in order to change their arrangements with Feeding Canadian Kids. 

6. As a *program partner*, I want to have access to a resources page so I can learn who to use Feeding Canadian Kids application.

    + Acceptance Criteria:
        + Accessing a resources webpage through the program partner profile
    + Acceptance Review:
        + The resources page has been created and restaurant partners can access it to review the resources made available to them by the admins.

7. As a *Feeding Canadian Kids admin*, I want to be able to have access to a sign-in page so I can review the operations.

    + Acceptance Criteria:
        - Feeding Canadian Kids admins can access a sign-in page (authentication with email and password)
    + Acceptance Review:
        + The sing-in page is now created and admins can access it to sing-in into their accounts. 

8. As a Feeding Canadian Kids admin, I want to be able to Receive applications from potential Restaurant Partners and potential Program Partners so I can sign them up for the program.

    + Acceptance Criteria:
        - Feeding Canadian Kids admin receives an email notification when someone requests a sign up
        - Feeding Canadian Kids admin is able to add new program partners and restaurant partners to a database easy to use
    - Acceptance Review: 
        - Both of these criteria has been met. When a user applies, the admin email receives a notification email and the admins then can review the application and decide to deny or accept it. In addition:
            - Our live notification systems allows the admins to get the news of new application quickly and within the environment of the application.
            - Admins can make changes to application and provide comments when they deny an application. 


9. As a *Feeding Canadian Kids admin*, I want to be able to pair restaurant partners with program partners so I can make plans for delivering to kids in need.

    + Acceptance Criteria:
        + Feeding Canadian Kids admin can see a suggested (based on distance, or other factors) list of restaurant partners for each program partner or vice versa
    + Acceptance Review:
        + This feature is pending. Not part of the MVP

10. As a *Feeding Canadian Kids admin*, it is very important to me to have access to details of operations so I can manage deliveries and donations smoothly.

    + Acceptance Criteria:
        - Feeding Canadian Kids admins have access to contact information of program partners and restaurant partners
        - Feeding Canadian Kids admins can see a calendar of upcoming events/deliveries
    + Acceptance Review: 
        + Both of these criteria has been met. Admins can access users individual profile pages. They also can access a table that details all the pairings and upcoming deliveries to them. 


11. As a *Feeding Canadian Kids admin*, I should be able to add or remove admins so I can manage large operations with a team.

    + Acceptance Criteria:
        - Admin can access the account creation page from their profile
        - Admin can create new admin accounts by supplying a username and password
        - Admin can edit and delete existing admin accounts
    - Acceptance Review:
        - All three of the criteria has been met. Admins can access an admin add/remove page where they can add or remove admins. 

12. As a *Feeding Canadian Kids admin*, I want to have access to a resources page so I can review the functionality of the software system I am managing.

    + Acceptance Criteria:
        - Accessing a resources webpage through the admin profile
    - Acceptance Review: 
        - Admins can access the resources page and they are also able to add new resources for different users. 


## Client Hand Off Plan

If the client chooses our product, we have planned a hand off through these steps: 

1. We will provide a list of credentials for the deployment of the application and maintaining it. 
2. We will provide them with a list of environment requirements (i.e. the libraries that we used to create our MVP)
3. We will provide the user with a script that allows them to run the application and deploy it smoothly and without having to worry about the dependencies. 
4. We will provide them with a high level description of our product's functionality (this is already available in README.md) 
5. We will provide instructions on how to handle cases where error/crash happens in the procedures. 
6. We will provide the client with scrips to input/transfer data into our application 
