from agents import Agent, Runner, function_tool, WebSearchTool

@function_tool

def get_user_data(min_age: int) -> list[dict]:
    "Retrieve user data based on a minimum age"
    users = [

        {

            "name": "Muneeb",
            "age": 22,
            "city": "Lahore",
            "profession": "Software Engineer",
            "education": "BS Computer Science",
            "marital_status": "Single",
            "income": "150,000 PKR/month",
            "height_cm": 175,
            "hobbies": ["Coding", "Reading", "Gaming"]
        },
        {
            "name": "Muhammad Ubaid Hussain",
            "age": 25,
            "city": "Karachi",
            "profession": "Data Analyst",
            "education": "BS Data Science",
            "marital_status": "Single",
            "income": "180,000 PKR/month",
            "height_cm": 178,
            "hobbies": ["Cricket", "Traveling", "Music"]
        },
        {
            "name": "Azan",
            "age": 19,
            "city": "Islamabad",
            "profession": "Student",
            "education": "BS IT",
            "marital_status": "Single",
            "income": "0 PKR",
            "height_cm": 170,
            "hobbies": ["Drawing", "Movies", "Cycling"]
        },
        {
            "name": "Ali Raza",
            "age": 28,
            "city": "Faisalabad",
            "profession": "Civil Engineer",
            "education": "BSc Civil Engineering",
            "marital_status": "Single",
            "income": "220,000 PKR/month",
            "height_cm": 180,
            "hobbies": ["Traveling", "Photography", "Hiking"]
        },
        {
            "name": "Usman Tariq",
            "age": 30,
            "city": "Rawalpindi",
            "profession": "Doctor",
            "education": "MBBS",
            "marital_status": "Single",
            "income": "300,000 PKR/month",
            "height_cm": 176,
            "hobbies": ["Swimming", "Reading", "Volunteering"]
        },
        {
            "name": "Fahad Ahmed",
            "age": 27,
            "city": "Multan",
            "profession": "Businessman",
            "education": "MBA",
            "marital_status": "Single",
            "income": "400,000 PKR/month",
            "height_cm": 182,
            "hobbies": ["Golf", "Networking", "Investing"]
        },
    ]

    for user in users:
        if user["age"] < min_age:
            users.remove(user)

    return users

rishtey_wali_agent = Agent(
    name="Auntie",
    model="gpt-4o-min",
    instructions= "You are warm and wise 'Rishtey Wali Auntie' who helps people find matches",
    tools=[get_user_data, WebSearchTool()]
    
)

result = Runner.run_sync(
    starting_agent=rishtey_wali_agent,
    input="find a match of 25 minimum age and tell me the details about the match from linkedin "
)

print (result.final_output)
    