SpringVerify REST API's
=======================


Login
-----

This API is used to login into the platform. We use Json Web Token for authentication. Please refer `here <https://jwt.io/introduction/>`_ to know more about Json Web Token. It is used as Bearer Token in all the API's appart from login API.

**Path** : /v1/auth/login

**Method** : POST

**Example Request**
 	.. code::
		
		curl --location --request POST 'http://localhost:3009/auth/login' \
		--header 'Content-Type: application/json' \
		--data-raw '{
			"email":"jackhym23@gmail.com",
			"password":"999999999"
		}'

**Example Response**
	.. code::

		{
			"message": "logged in successfully",
			"data": {
				"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjp7ImVtYWlsIjoiamFja2h5bTIzQGdtYWlsLmNvbSIsImNvbXBhbnlJZCI6Mn0sImlhdCI6MTU4MjU1MjcyOCwiZXhwIjoxNTg2MTUyNzI4fQ.7zs45ogp_Rcma7sJkzNcH5cnZ6gMQK-NXZjbxDsyFJw"
			}
		}

**Query Parameters**
	
	* email (string): Email registered in springverify. 
	* password (string): Password registered in springverify.

**Response Parameters**

	* message (string): Success message. 
	* data (Object): Contains data of success response.
	* token (string): Used as bearer token in add candidate API.

Add Candidate
-------------

This API is used to select the types of check this candidate should go through. 

**Path** : /v1/candidate

**Method** : POST

**Example Request**
 	.. code::
		
		curl --location --request POST 'http://api-dev.in.springverify.com/v1/candidate' \
		--header 'Content-Type: application/json' \
		--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjp7ImVtYWlsIjoiYW51cmFnLnNhbmRodUBzcHJpbmdyb2xlLmNvbSIsImNvbXBhbnlJZCI6Mn0sImlhdCI6MTU4MTU4MDM5NywiZXhwIjoxNTg1MTgwMzk3fQ.p4K0NefA8eOXFcCqxOYiLtnhmXM0KbqsiBuVxsUqT_o' \
		--data-raw '{
		    "name": "Anurag Sandhu",
		    "email": "anurag.sandhu@springrole.com",
		    "consentUrl" : "https://springverify-assets.s3.amazonaws.com/ccl_1574149640_332.pdf",
		    "verifications": {
		        "identity": {
		            "pan": true,
		            "drivingLicense": true,
		            "passport": true,
		            "voterId": true
		        },
		        "address": {
		            "current": false,
		            "permanent": false
		        },
		        "education": {
		            "10": true,
		            "12": true,
		            "bachelor": false,
		            "masters": true,
		            "doctorate": true
		        },
		        "workExperience": {
		            "employments": 1
		        },
		        "criminalRecord": {
		            "current": false,
		            "permanent": false
		        }
		    }
		}'

**Example Response**
	.. code::

		{
	    "message": "Candidate registered, token shared for further communication of {Anurag Sandhu}",
	    "body": {
	        "name": "Anurag Sandhu",
	        "email": "anurag.sandhu@springrole.com",
	        "consentUrl": "https://springverify-assets.s3.amazonaws.com/ccl_1574149640_332.pdf",
	        "verifications": {
	            "identity": {
	                "pan": true,
	                "drivingLicense": true,
	                "passport": true,
	                "voterId": true
	            },
	            "address": {
	                "current": false,
	                "permanent": false
	            },
	            "education": {
	                "10": true,
	                "12": true,
	                "bachelor": false,
	                "masters": true,
	                "doctorate": true
	            },
	            "workExperience": {
	                "employments": 1
	            },
	            "criminalRecord": {
	                "current": false,
	                "permanent": false
	            }
	        }
	    },
	    "uuid": "57e7423d-5ed0-46d9-9d6b-f96255362c40",
	    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjp7ImNhbmRpZGF0ZUlkIjozNjUsImNvbXBhbnlJZCI6Miwicm9sZSI6ImNhbmRpZGF0ZSJ9LCJpYXQiOjE1ODI4OTA1NDJ9.NqSLyvSicWdvSHEJcS8C3-Q1DAS4N45HtaUlO1ICT0U"
		}

**Query Parameters**
	
	* identity (Object): Used to provide types of checks selected.
		
		**Object Keys**
			- pan (Boolean)
			- passport (Boolean)
			- voterId (Boolean)
			- drivingLicense (Boolean)

	* address (Object): Used to provide what type of aaddress is being stored.
		
		**Object Keys**
			- current (Boolean)
			- permanent (Boolean)

	* education (Object): Used to provide types of education checks selected.
		
		**Object Keys**
			- 10 (Boolean)
			- 12 (Boolean)
			- bachelor (Boolean)
			- masters (Boolean)
			- doctorate (Boolean)

	* workExperience (Object): Used to provide types of work experience selected.
		
		**Object Keys**
			- employments (Intiger): count of the employments candidate has.

	* criminalRecord (Object): Used to provide on which address to run criminal check.
		
		**Object Keys**
			- current (Boolean)
			- permanent (Boolean)

**Response Parameters**

	* message (string): Success message.
	* data (Object): Contains the request in the response and token.
	* token (string): This token is candidate specific. For further api's this token will be used.

Identity Verification
---------------------

This API returns the ocr result of the identity document uploaded. 

.. note::
	 Please give the image url in this API.
	 Use the token which was returned after add candidate API.

**Currenly Supported Docs**
	
	* DRIVING LICENSE.
	* PAN
	* PASSPORT
	* VOTER ID 

**Path** : /v1/documents/identity

**Method** : POST

**Example Request**
 	.. code::
		
		curl --location --request POST 'http://api-dev.in.springverify.com/v1/documents/identity' \
		--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjp7ImNhbmRpZGF0ZUlkIjozMjMsImNvbXBhbnlJZCI6Miwicm9sZSI6ImNhbmRpZGF0ZSJ9LCJpYXQiOjE1ODAzODUxMjN9.dInOuPThk52E7KLh1084zpxyfcWyYQQAPYiD9b2d05w' \
		--form 'type=ind_driving_license' \
		--form 's3Front=https://springverify-assets-id.s3.amazonaws.com/323/ind_driving_license-front' \
		--form 's3Back=https://springverify-assets-id.s3.amazonaws.com/323/ind_driving_license-front'

**Example Response**
	.. code::

		{
			"message": "identity doc uploaded succesfully",
			"data": {}
		}

**Query Parameters**
	
	* type (string): Used to give the type of id doc provided.
		
		**Possible Values**
			- ind_driving_license
			- ind_passport
			- ind_voter_id
			- ind_pan

	* s3Front (string): front side of the identity doc.
	* s3Back (String): back of the identity doc. (optional field)

**Response Parameters**

	* message (string): Success message.


Add Employment
--------------

This API is used to add employment details and docs.

.. note::
	 Please give the image url in this API.
	 Use the token which was returned after add candidate API.

**Currenly Supported Docs**
	
	* Salary Slip
	* Experience Letter
	* Relieving Letter
	* Appointment Letter
	* Others (not specific doc)

**Path** : /v1/documents/employment

**Method** : POST

**Example Request**
 	.. code::
		
		curl --location --request POST 'http://api-dev.in.springverify.com/v1/documents/employment' \
		--header 'Content-Type: application/json' \
		--data-raw '{
		    "employments" : [
		        {
		            "document_type": "ABC",
					"companyName": "ABC",
		            "designation": "1",
		            "currentlyHere": true,
		            "startDate": "25/11/19",
		            "s3Links" : [
		            "https://springverify-assets-id.s3.amazonaws.com/323/ind_driving_license-front",
		            "https://springverify-assets-id.s3.amazonaws.com/323/ind_driving_license-front",
		            "https://springverify-assets-id.s3.amazonaws.com/323/ind_driving_license-front"
		            ]
		        }
		    ]
		}'

**Example Response**
	.. code::

		{
		    "message": "Employment saved",
		    "response": [
		        {
		            "document_type": "ABC",
		            "companyName": "ABC",
		            "designation": "1",
		            "currentlyHere": true,
		            "startDate": "25/11/19",
		            "s3Links": [
		                "https://springverify-assets-id.s3.amazonaws.com/323/ind_driving_license-front",
		                "https://springverify-assets-id.s3.amazonaws.com/323/ind_driving_license-front",
		                "https://springverify-assets-id.s3.amazonaws.com/323/ind_driving_license-front"
		            ],
		            "uuid": "04c537a5-2fe9-43f9-bac6-bf7e4f98f861"
		        }
		    ]
		}

**Query Parameters**
	
	* document_type (string): Used to give the type of employment doc provided.
		
		**Possible Values**
			- SalarySlip
			- ExperienceLetter
			- RelievingLetter
			- AppointmentLetter
			- Other

	* companyName (string): name of the company where candidate was working.
	* designation (String): designation of the candidate.
	* currentlyHere (Boolean): true for currently working here.
	* startDate (String): Format dd/mm/yy.
	* s3Links (Array): Array of employment doc's links.

**Response Parameters**

	* message (string): Success message.
	* response (object): It contains the request object.


Add Education
-------------

This API is used to add education details and docs.

.. note::
	 Please give the image url in this API.
	 Use the token which was returned after add candidate API.

**Currenly Supported Docs**
	
	* 10th class
	* 12th class
	* Bachelor
	* masters
	* doctorate

**Path** : /v1/documents/education

**Method** : POST

**Example Request**
 	.. code::
		
		curl --location --request POST 'http://api-dev.in.springverify.com/v1/documents/education' \
		--header 'Content-Type: application/json' \
		--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjp7ImNhbmRpZGF0ZUlkIjozMjMsImNvbXBhbnlJZCI6Miwicm9sZSI6ImNhbmRpZGF0ZSJ9LCJpYXQiOjE1ODAzODUxMjN9.dInOuPThk52E7KLh1084zpxyfcWyYQQAPYiD9b2d05w' \
		--data-raw '{
			"education" :     {
		        "10": [
		            "https://springverify-assets-id.s3.amazonaws.com/323/ind_driving_license-front"
		        ],
		        "12": [
		            "https://springverify-assets-id.s3.amazonaws.com/323/ind_driving_license-front",
		            "https://springverify-assets-id.s3.amazonaws.com/323/ind_driving_license-front"
		        ],
		        "bachelor": [
		            "https://springverify-assets-id.s3.amazonaws.com/323/ind_driving_license-front"
		        ],
		        "masters": [
		            "https://springverify-assets-id.s3.amazonaws.com/323/ind_driving_license-front"
		        ],
		        "doctorate": [
		        ]
		    }
		}'

**Example Response**
	.. code::

		{
		    "message": "Education data saved",
		    "listOfUploadedDocs": [
		        "10",
		        "masters",
		        "doctorate"
		    ],
		    "listOfNotUploadedDocs": [
		        "bachelor"
		    ],
		    "ReasonForNoteUploadingDocs": "You may not have selected the config checks while creating the user with springverify",
		    "Note": "Empty array of any qualification won't get inserted in the DB"
		}

**Query Parameters**
	
	* education (array): Used to give the type of education doc provided.
		
		**Keys**
			- 10
			- 12
			- bachelor
			- masters
			- doctorate


**Response Parameters**

	* message (string): Success message.
	* response (object): It contains the request object.


Get Candidate
-------------

This API is used to get candidates in bulk.

.. note::
	 Use the token which was returned after add candidate API.

**Path** : /v1/candidate/fetch

**Method** : POST

**Example Request**
 	.. code::
		
		curl --location --request GET 'http://localhost:3009/v1/candidate/fetch' \
		--header 'Content-Type: application/json' \
		--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjp7ImVtYWlsIjoiYW51cmFnLnNhbmRodUBzcHJpbmdyb2xlLmNvbSIsImNvbXBhbnlJZCI6Mn0sImlhdCI6MTU4MTU4MDM5NywiZXhwIjoxNTg1MTgwMzk3fQ.p4K0NefA8eOXFcCqxOYiLtnhmXM0KbqsiBuVxsUqT_o' \
		--data-raw '{
			"uuid" : ["89234831-1a7a-11ea-bc81-1657eb2ddd16", "16fe0e16-61dc-431c-9f33-255ec1b01fd4"]
		}'

**Example Response**
	.. code::

		[
		    {
		        "id": 331,
		        "uuid": "94e07ae6-cac5-40a9-bdb4-2d85526fde2a",
		        "email": "anurag.sandhu@springrole.com",
		        "alternate_email": null,
		        "name": "Anurag Sandhu",
		        "type": null,
		        "created_at": "2020-02-28T08:56:35.000Z",
		        "updated_at": "2020-02-28T08:56:35.000Z",
		        "ongrid_id": null,
		        "gender": null,
		        "deleted_at": null,
		        "dob": null,
		        "father_name": null,
		        "email_reject_type": "NA",
		        "company_candidate_mapping": {
		            "id": 319,
		            "uuid": "ab5ee3eb-6fab-4a63-8a32-ede6ccf45b97",
		            "company_id": 2,
		            "candidate_id": 331,
		            "employee_id": null,
		            "phone_number": null,
		            "country_code": "IN",
		            "alt_phone_number": null,
		            "alt_country_code": "IN",
		            "resume": null,
		            "category_id": null,
		            "created_at": "2020-02-28T08:56:36.000Z",
		            "updated_at": "2020-02-28T08:56:42.000Z",
		            "deleted_at": null,
		            "candidate_ids": null,
		            "work_experience": null,
		            "education": null,
		            "address": null,
		            "history": null,
		            "refcheck": null,
		            "worldcheck": null,
		            "creditcheck": null,
		            "drugscheck": null,
		            "typeform_url": null,
		            "signrequest_url": null,
		            "status": "candidateAdded",
		            "signedrequest_status": 0,
		            "springverify_signature": null,
		            "consent_letter_url": "https://springverify-assets-id.s3.amazonaws.com/331/consent-letter",
		            "consent_added_at": "2020-02-28T08:56:42.000Z",
		            "spring_candidate_ip": null,
		            "form_filled": null,
		            "candidate_added_by": 2,
		            "form_filled_by": 3,
		            "consent_added_by": 2,
		            "who_fills_form": 3,
		            "past_jobs": "1",
		            "springscan_id": "5e58d5c52e3c6c001cfa0f20"
		        },
		        "candidates_ids": [],
		        "candidates_addresses": [],
		        "candidates_employments": [],
		        "candidates_educations": [],
		        "candidate_histories": []
		    }
		]

**Query Parameters**
	
	* uuid (array): It takes an array of uuid's of the candidates which were returned when adding a candidate.
		


**Response Parameters**

	* Returns an array of candidate Object corresponding to the uuid's given.