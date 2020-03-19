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
			"msg": "User logged in successfully",
			"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjp7ImVtYWlsIjoiYW51cmFnLnNhbmRodUBzcHJpbmdyb2xlLmNvbSIsImNvbXBhbnlJZCI6MiwidXNlcklkIjo5MSwiY29tcGFueU5hbWUiOiJteWZha2VpY28gdGVzdGluZyBjbyAuaW4gW1BWVCBMRFRdIn0sImlhdCI6MTU4NDYxNTc5MywiZXhwIjoxNTg4MjE1NzkzfQ.ieVyXxv79SBLSaLWwJOwuzscFBlZfdF71CIZQ22B9_s"
		}

**Query Parameters**
	
	* email (string): Email registered in springverify. 
	* password (string): Password registered in springverify.

**Response Parameters**

	* message (string): Success message. 
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
		"uuid": "8b32cd73-7426-45ed-bc4d-50516ad15ad0",
		"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjp7ImNhbmRpZGF0ZUlkIjozODEsImNvbXBhbnlJZCI6Miwicm9sZSI6ImNhbmRpZGF0ZSJ9LCJpYXQiOjE1ODQ2MTY0NTR9.CYYjDgp5kmRBxtbQpFmsaP2JB46Fct4yBOOmeW27rQc"
		}

**Query Parameters**
	
	* Identity (Object): Used to provide types of checks selected.
		
		**Object Keys**
			- pan (Boolean)
			- passport (Boolean)
			- voterId (Boolean)
			- drivingLicense (Boolean)

	* Address (Object): Used to provide what type of aaddress is being stored.
		
		**Object Keys**
			- current (Boolean)
			- permanent (Boolean)

	* Education (Object): Used to provide types of education checks selected.
		
		**Object Keys**
			- 10 (Boolean)
			- 12 (Boolean)
			- bachelor (Boolean)
			- masters (Boolean)
			- doctorate (Boolean)

	* WorkExperience (Object): Used to provide types of work experience selected.
		
		**Object Keys**
			- employments (Intiger): count of the employments candidate has.

	* CriminalRecord (Object): Used to provide on which address to run criminal check.
		
		**Object Keys**
			- current (Boolean)
			- permanent (Boolean)

**Response Parameters**

	* message (string): Success message.
			FOR: Making the operation more meaningful [No need to save] 
	* uuid (string): Contains the unique id for the candidate.
			FOR: This will be used while fetching the candidate from springverify [Saving Required]
	* token (string): This token is candidate specific. For further api's this token will be used.
			FOR: No Expiration Time [Saving Required]

	
Identity Upload/Verification
---------------------

This API saves the document uploaded into SV DB.
	SCENARIO 1: If company has opted for Identity Verification Automatic service and sending front(Not Array of docs), it will verify the ID internally(Asyncronously)
				Response from this can be fetched after 3-5 min.
	SCENARIO 2: If company has not opted for Identity Verification Automatic service, it will save the ID's in DB.
				Response will be returned immediately.

.. note::
	 Please give the image url in this API.
	 Use the token which was returned after add candidate API.

**Currenly Supported Docs**
	
	* DRIVING LICENSE (type : ind_driving_license)
	* PAN (type : ind_pan)
	* PASSPORT (type : ind_passport)
	* VOTER ID (type : ind_voter_id)

**Path** : /v1/documents/identity

**Method** : POST

**Example Request**

		.. code::
			
			curl --location --request POST 'http://api-dev.in.springverify.com/v1/documents/identity' \
			--header 'Content-Type: application/json' \
			--data-raw '{
			"type": "ind_driving_license",
			"docs": ["https://springverify-assets-id.s3.amazonaws.com/323/*********-front", "https://springverify-assets-id.s3.amazonaws.com/323/*********--front"]
			}'

		OR

		.. code::
			
			curl --location --request POST 'http://api-dev.in.springverify.com/v1/documents/identity' \
			--header 'Content-Type: application/json' \
			--data-raw '{
			"type" : "ind_voter_id",
			"front": "https://springverify-assets-id.s3.amazonaws.com/323/ind_driving_license-front",
			"back": "https://springverify-assets-id.s3.amazonaws.com/323/ind_driving_license-front"
			}'

		OR (Back is optional)
			
		.. code::
			
			curl --location --request POST 'http://api-dev.in.springverify.com/v1/documents/identity' \
			--header 'Content-Type: application/json' \
			--data-raw '{
			"type" : "ind_voter_id",
			"front": "https://springverify-assets-id.s3.amazonaws.com/323/ind_driving_license-front"
			}'
		NOTE: Identity Verification Automatic can not applied to DOCS Array's payload. (Not to CURL 1)

**Example Response**
	.. code::

		{
		"message": "Identity saved",
		"uuid": [ "9fd58e5d-cee5-4b7b-9ef3-6eb446d952aa" ]
		}

**Query Parameters**
	
	* type (string): Used to give the type of id doc provided.
		
		**Possible Values**
			- ind_driving_license
			- ind_passport
			- ind_voter_id
			- ind_pan


**Response Parameters**

	* message (string): Success message.
			FOR: Making the operation more meaningful [No need to save] 
	* uuid (string): Contains the unique id for the identity saved in DB.
			[Saving is your choice.]


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
		            "https://springverify-assets-id.s3.amazonaws.com/***/ind_driving_license-front",
		            "https://springverify-assets-id.s3.amazonaws.com/***/ind_driving_license-front",
		            "https://springverify-assets-id.s3.amazonaws.com/***/ind_driving_license-front"
		            ]
		        }
		    ]
		}'

**Example Response**
	.. code::

		{
		    "message": "Employment saved",
		    "uuid": [04c537a5-2fe9-43f9-bac6-bf7e4f98f861, 04c537a5-2fe9-43f9-bac6-bf7e4f98f861, 04c537a5-2fe9-43f9-bac6-bf7e4f98f861  ]
		}

**Query Parameters**
	
	* document_type (string): Used to give the type of employment doc provided.
		
		**Possible Values**
			- SalarySlip
			- ExperienceLetter
			- RelievingLetter
			- AppointmentLetter
			- Other

	* CompanyName (string): name of the company where candidate was working.
	* Designation (String): designation of the candidate.
	* CurrentlyHere (Boolean): true for currently working here.
	* StartDate (String): Format dd/mm/yy.
	* S3Links (Array): Array of employment doc's links.

**Response Parameters**

	* message (string): Success message.
	* uuid (string): Contains the unique id for the Employment saved in DB.
			[Saving is your choice.]

Add Address
--------------

This API is used to add Address details and docs.

.. note::
	 Please give the image url in this API.
	 Use the token which was returned after add candidate API.

**Currenly Supported Docs**
	
	* Aadhaar Card
	* Voter Id
	* Driving License
	* Passport
	* Ration Card
	* Vehicle Registration Certificate
	* Utility Bill
	* Bank Statement

**Path** : /v1/documents/address

**Method** : POST

**Example Request**
 	.. code::
		
		curl --location --request POST 'http://api-dev.in.springverify.com/v1/documents/employment' \
		--header 'Content-Type: application/json' \
		--data-raw '{
			"isPermanent" : false,
			"addressLinks": [
				"https://springverify-assets-id.s3.amazonaws.com/323/ind_driving_license-front"
			],
			"docType": "Driving License"
		}'

**Example Response**
	.. code::

		{
		    "message": "Address saved",
		    "uuid": ["04c537a5-2fe9-43f9-bac6-bf7e4f98f861"]
		}

**Query Parameters**
	* isPermanent (Boolean): is this current address or permanent.
	* addressLinks (Array): Links of the images uploaded to some bucket.
	* docType (string): true for currently working here.
		**Keys**
			* Aadhaar Card
			* Voter Id
			* Driving License
			* Passport
			* Ration Card
			* Vehicle Registration Certificate
			* Utility Bill
			* Bank Statement

**Response Parameters**

	* message (string): Success message.
	* uuid (string): Contains the unique id for the Address saved in DB.

Add Education
-------------

This API is used to add education details and docs.

.. note::
	 Please give the image url in this API.
	 Use the token which was returned after add candidate API.
	 IF you haven't selected the education as 'true' while registering a candidate with springverify. We will ignore
	 that particular education, save which were selected and you can find list Of Not Uploaded Docs in the response.
	 You will get list of uploaded docs as well in the response.
	 Empty array of any qualification won't get inserted in the DB

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
	* uuid (object): Unique ID's for docs which got saved in DB.
	* listOfUploadedDocs (object): Docs which got uploaded.
	* listOfNotUploadedDocs (object): Docs which failed to got uploaded.
	* ReasonForNoteUploadingDocs (object): If any document didn't get uploaded.
	* Note (object): Unique ID's for docs which got saved in DB.


Get Candidate
-------------

This API is used to get candidates in bulk.

.. note::
	 Use the token which was returned after add candidate API.

**Path** : /v1/candidate/fetch

**Method** : POST

**Example Request**
		
FOR Multiple candidates

 	.. code::
		
		curl --location --request GET 'http://localhost:3009/v1/candidate/fetch' \
		--header 'Content-Type: application/json' \
		--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjp7ImVtYWlsIjoiYW51cmFnLnNhbmRodUBzcHJpbmdyb2xlLmNvbSIsImNvbXBhbnlJZCI6Mn0sImlhdCI6MTU4MTU4MDM5NywiZXhwIjoxNTg1MTgwMzk3fQ.p4K0NefA8eOXFcCqxOYiLtnhmXM0KbqsiBuVxsUqT_o' \
		--data-raw '{
			"uuid" : ["89234831-1a7a-11ea-bc81-1657eb2ddd16", "16fe0e16-61dc-431c-9f33-255ec1b01fd4"]
		}'

OR (FOR Single candidate)

 	.. code::
		
		curl --location --request GET 'http://localhost:3009/v1/candidate/fetch' \
		--header 'Content-Type: application/json' \
		--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjp7ImVtYWlsIjoiYW51cmFnLnNhbmRodUBzcHJpbmdyb2xlLmNvbSIsImNvbXBhbnlJZCI6Mn0sImlhdCI6MTU4MTU4MDM5NywiZXhwIjoxNTg1MTgwMzk3fQ.p4K0NefA8eOXFcCqxOYiLtnhmXM0KbqsiBuVxsUqT_o' \
		--data-raw '{
			"uuid" : ["89234831-1a7a-11ea-bc81-1657eb2ddd16"]
		}'

OR (FOR Single candidate)

 	.. code::
		
		curl --location --request GET 'http://localhost:3009/v1/candidate/fetch' \
		--header 'Content-Type: application/json' \
		--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjp7ImVtYWlsIjoiYW51cmFnLnNhbmRodUBzcHJpbmdyb2xlLmNvbSIsImNvbXBhbnlJZCI6Mn0sImlhdCI6MTU4MTU4MDM5NywiZXhwIjoxNTg1MTgwMzk3fQ.p4K0NefA8eOXFcCqxOYiLtnhmXM0KbqsiBuVxsUqT_o' \
		--data-raw '{
			"uuid" : "89234831-1a7a-11ea-bc81-1657eb2ddd16"
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
					"candidate_histories": [],
			"user": {
				"id": 2,
				"uuid": "dde7c7ff-1d81-45a9-9e24-e8ad2077d4f1",
				"name": "Jack",
				"username": null,
				"email": "jackhym23@gmail.com",
				"password": "$2y$13$wmNiKDRqbgZjMEbtvdfUZOcHG82lhF9s/VWSPA0RL2BE6uZlz0FlC",
				"access_level": null,
				"mobile": "9876543211",
				"status": 1,
				"auth_key": null,
				"password_reset_token": null,
				"created_at": null,
				"updated_at": "2020-03-19T06:39:11.000Z",
				"deleted_at": "2020-03-19T01:09:11.000Z",
				"customer_id": "cust_Dq8sAd6hp3KLxu",
				"email_reject_type": "NA",
				"designation": "super admin"
			},
			"document": {
				"ind_driving_license": {
					"result": {
						"address": "S NO. 32/14 A/3, AMBEGAON BK, BHARTI VIDYAPEETH BACKSIDE, PUNE.",
						"date_of_birth": "1986-05-12",
						"date_of_validity": null,
						"fathers_name": "MILIND PALANDE",
						"id_number": "MH-1220050000188",
						"is_scanned": "false",
						"issue_dates": {
							"LMV": null,
							"MCWG": null,
							"TRANS": null
						},
						"name_on_card": "POOJA M PALANDE",
						"pincode": "411046",
						"state": "Maharashtra",
						"street_address": "32/14 A/3, AMBEGAON BK, BHARTI VIDYAPEETH BACKSIDE, PUNE",
						"type": [
							"MCWG",
							"TRANS"
						],
						"validity": {
							"NT": null,
							"T": "1986-05-12"
						}
					},
					"matchedInformation": {
						"message": "OCR Data has been verified with government source",
						"source": "SARATHI",
						"status": "source_down",
						"ocr_id_match": false
					},
					"govResult": {
						"action": "verify_with_source",
						"completed_at": "2020-03-18T14:24:54+05:30",
						"created_at": "2020-03-18T14:24:45+05:30",
						"error": "SOURCE_DOWN",
						"group_id": "5e6f67cb29155a001d00a8cc",
						"request_id": "b6680566-211e-4795-8edf-72812b95e7f7",
						"result": {
							"source_output": {
								"address": null,
								"badge_details": null,
								"card_serial_no": null,
								"city": null,
								"cov_details": null,
								"date_of_issue": null,
								"date_of_last_transaction": null,
								"dl_status": null,
								"dob": null,
								"face_image": null,
								"gender": null,
								"hazardous_valid_till": null,
								"hill_valid_till": null,
								"id_number": null,
								"issuing_rto_name": null,
								"last_transacted_at": null,
								"name": null,
								"nt_validity_from": null,
								"nt_validity_to": null,
								"relatives_name": null,
								"source": "SARATHI",
								"status": "source_down",
								"t_validity_from": null,
								"t_validity_to": null
							}
						},
						"status": "failed",
						"task_id": "5e71e1ae0faf61001d96ca10",
						"type": "ind_driving_license"
					}
				}
			}
				}
			]



**Query Parameters**
	
	* uuid (array): It takes an array of uuid's of the candidates which were returned when adding a candidate.
		


**Response Parameters**

	* Returns an array of candidate Object corresponding to the uuid's given, with their corresponding checks data.
	* User: Uploader details.
	* document: (Response of Identity Validation)(Only if your company selected this service and sent 'front' doc in payload.)
	* Returns an array of candidate Object corresponding to the uuid's given, with their corresponding checks data.