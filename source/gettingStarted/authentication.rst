SpringVerify REST API's
=======================


Login
-----

This API is used to login into the platform. We use Json Web Token for authentication. Please refer `here <https://jwt.io/introduction/>`_ to know more about Json Web Token. It is used as Bearer Token in all the API's appart from login API.

**Path** : /v1/auth/login

**Method** : POST

**Example Request**
 	.. code-block:: html
		
		curl --location --request POST 'https://api-dev.in.springverify.com/v1/auth/login' \
		--header 'Content-Type: application/json' \
		--data-raw '{
			"email":"jackhym23@gmail.com",
			"password":"999999999"
		}'

**Example Response**
	.. code-block:: html

		{
			"message": "logged in successfully",
			"data": {
				"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjp7ImVtYWlsIjoiamFja2h5bTIzQGdtYWlsLmNvbSIsImNvbXBhbnlJZCI6Mn0sImlhdCI6MTU4MjU1MjcyOCwiZXhwIjoxNTg2MTUyNzI4fQ.7zs45ogp_Rcma7sJkzNcH5cnZ6gMQK-NXZjbxDsyFJw"
			}
		}

**Query Parameters**
	- **email** (String): Email registered in springverify.

	- **password** (String): Password registered in springverify.

**Response Parameters**
	- **message** (String): Success message. 

	- **data** (Object): Contains token.

	- **token** (String): Used as bearer token in add candidate API.

Add Candidate
-------------

Post API to gather candidate's basic details and configuration. The configuration is decided at the company (your) end. The configuration sent in this api will be
validated against enteries in following APIs. For example , if Pan is True, we expect candidate's pan card in identity verifications API.

**Path** : /v1/candidate

**Method** : POST

**Example Request**
 	.. code-block:: html
		
		curl --location --request POST 'https://api-dev.in.springverify.com/v1/candidate' \
		--header 'Content-Type: application/json' \
		--header 'Authorization: Bearer <Token>' \
		--data-raw '{
		    "name": "Anurag Sandhu",
		    "email": "anurag.sandhu@springrole.com",
		    "consentUrl" : <consent_url>,
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
	.. code-block:: html

		{
	    	"message": "Candidate registered, token shared for further communication of {Anurag Sandhu}",
	    	"uuid": "57e7423d-5ed0-46d9-9d6b-f96255362c40",
	    	"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjp7ImNhbmRpZGF0ZUlkIjozNjUsImNvbXBhbnlJZCI6Miwicm9sZSI6ImNhbmRpZGF0ZSJ9LCJpYXQiOjE1ODI4OTA1NDJ9.NqSLyvSicWdvSHEJcS8C3-Q1DAS4N45HtaUlO1ICT0U"
		}

Query Parameters
	- **consentUrl** (String): 
		URL of signed consent from the user being verified.

	- **identity** (Object): Used to provide types of checks selected.
			- **pan** (Boolean)  - PAN Card validation required
			- **passport** (Boolean) - Passport validation required
			- **voterId** (Boolean) - VoterID validation required
			- **drivingLicense** (Boolean) - Driving License Card validation required

	- **address** (Object): Used to provide what type of aaddress is being stored.
			- **current** (Boolean) - Current Address validation required
			- **permanent** (Boolean) - Permanent Address validation required

	- **education** (Object): Used to provide types of education checks selected.
			- **10** (Boolean) - Class Xth mark sheet validation required
			- **12** (Boolean)  - Class XIIth mark sheet validation required
			- **bachelor** (Boolean) - Bachelor Degree validation required
			- **masters** (Boolean) - Masters Degree validation required
			- **doctorate** (Boolean) - Doctorate/PHD or any other equivalent degree validation required

	- **workExperience** (Object): Used to provide types of work experience selected.
			- **employments** (Integer) - count of the employments candidate has.

	- **criminalRecord** (Object): Used to provide on which address to run criminal check.
			- **current** (Boolean) - Criminal check on current address required
			- **permanent** (Boolean) - Criminal check on permanent address required

Response Parameters
	- **message** (String): Success message.
	- **uuid** (String): Unique UUID of the candidate.
	- **token** (string): This token is candidate specific. **For further api's this token will be used.**

Identity Verification
---------------------

Post API to store ID card of the candidate. This will include OCR in future.

.. note:: Please give the image url in this API. Use the token which was returned after add candidate API. If your image is in base64, we suggest you host it on your server. If you are unable to host the image securely, please contact us.

.. warning:: will throw error if you try to upload a doc which was not configured in addCandidate API

- Currenly Supported Docs
	* DRIVING LICENSE
	* PAN
	* PASSPORT
	* VOTER ID 


**Path** : /v1/documents/identity

**Method** : POST

**Example Request**
 	.. code-block:: html
		
		curl --location --request POST 'https://api-dev.in.springverify.com/v1/documents/identity' \
		--header 'Content-Type: application/json' \
		--header 'Authorization: Bearer <Token>' \
		--header 'Content-Type: application/json' \
		--data-raw '{
		"type" : "ind_voter_id",
		"front" : <front_doc_url>,
		"back" : <back_doc_url>,
		"docs" : [ <doc_urls> ]
		}'

**Example Response**
	.. code-block:: html

		{
			"message": "identity doc uploaded succesfully",
			"data": {}
		}

.. note:: if you know the front and back, please send in front and back keys. If front and back are not known, please send in docs array. If front/back are provided, we conduct OCR of the document which can be fetched using getCandidate API. Back is optional, so you can only send front of the doc.



Query Parameters
	**type** (String): Used to give the type of id doc provided.
		*Possible Keys*
			- ind_driving_license
			- ind_passport
			- ind_voter_id
			- ind_pan

	**docs** (String): 
		Array of images for the doc

	**front** (String): 
		front url of doc. either front or docs key is required.

	**back** (String): 
		back url of doc. optional.

Response Parameters
	**message** (String): 
		Success message.

Add Employment
--------------

This API is used to add employment details and any relevant docs of the user.

.. note:: Please give the image url in this API. Use the token which was returned after add candidate API.

**Currenly Supported Docs**
	* Salary Slip
	* Experience Letter
	* Relieving Letter
	* Appointment Letter
	* Others (not specific doc)

**Path** : /v1/documents/employment

**Method** : POST

**Example Request**
 	.. code-block:: html
		
		curl --location --request POST 'https://api-dev.in.springverify.com/v1/documents/employment' \
		--header 'Content-Type: application/json' \
		--data-raw '{
		    "employments" : [
		        {
		            "document_type": "ABC",
					"companyName": "ABC",
		            "designation": "1",
		            "currentlyHere": true,
		            "startDate": "25/11/19",
					"endDate" : "25/3/20",
		            "s3Links" : [
					<link1>,
					<link2>,
					<link3>
		            ]
		        }
		    ]
		}'

**Example Response**
	.. code-block:: html

		{
		    "message": "Employment saved",
		    "response": [
		        <same as request>
		    ]
		}

**Query Parameters**
	* document_type (string): 
			Used to give the type of employment doc provided. supported keys:

			- SalarySlip
			- ExperienceLetter
			- RelievingLetter
			- AppointmentLetter
			- Other

	* companyName (string): 
		name of the company where candidate was working.
	* designation (String): 
		designation of the candidate.
	* currentlyHere (Boolean): 
		true for currently working here.
	* startDate (String): 
		Format dd/mm/yy
	* endDate (String):
		Format dd/mm/yy
	* s3Links (Array): 
		Array of employment doc's links.

**Response Parameters**
	* message (string): 
		Success message.
	* response (object): 
		It contains the request object.


Add Education
-------------

This API is used to add education details and any relevant docs of the user.

.. note:: Please give the image url in this API. Use the token which was returned after add candidate API.

.. warning:: Api will reject upload of any docs that were not set True in config. 

**Currenly Supported Docs**
	* 10th class
	* 12th class
	* Bachelor
	* Masters
	* Doctorate

**Path** : /v1/documents/education

**Method** : POST

**Example Request**
 	.. code-block:: html
		
		curl --location --request POST 'https://api-dev.in.springverify.com/v1/documents/education' \
		--header 'Content-Type: application/json' \
		--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjp7ImNhbmRpZGF0ZUlkIjozMjMsImNvbXBhbnlJZCI6Miwicm9sZSI6ImNhbmRpZGF0ZSJ9LCJpYXQiOjE1ODAzODUxMjN9.dInOuPThk52E7KLh1084zpxyfcWyYQQAPYiD9b2d05w' \
		--data-raw '{
			"education" :     {
		        "10": [
		            <link>
		        ],
		        "12": [
		            <link>,
		            <link>
		        ],
		        "bachelor": [
		            <link>
		        ],
		        "masters": [
		           <link>
		        ],
		        "doctorate": [
					<link>
		        ]
		    }
		}'

**Example Response**
	.. code-block:: html

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
	* education (array): 
		Used to give the type of education doc provided. valid keys for array of docs are:
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
 	.. code-block:: html
		
		curl --location --request GET 'https://api-dev.in.springverify.com/v1/candidate/fetch' \
		--header 'Content-Type: application/json' \
		--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjp7ImVtYWlsIjoiYW51cmFnLnNhbmRodUBzcHJpbmdyb2xlLmNvbSIsImNvbXBhbnlJZCI6Mn0sImlhdCI6MTU4MTU4MDM5NywiZXhwIjoxNTg1MTgwMzk3fQ.p4K0NefA8eOXFcCqxOYiLtnhmXM0KbqsiBuVxsUqT_o' \
		--data-raw '{
			"uuid" : ["89234831-1a7a-11ea-bc81-1657eb2ddd16", "16fe0e16-61dc-431c-9f33-255ec1b01fd4"]
		}'

**Example Response**
	.. code-block:: html

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

	* Returns an array of candidate Object corresponding to the uuid's given.SpringVerify REST API's