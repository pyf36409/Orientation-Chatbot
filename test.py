import ollama

model = "llama3.1"

messages = [{'role': 'user', 'content': """
You are a Orientation Chatbot, People will ask you for advise.
University Name: James Cook University (JCU)
Event Name: TR1S 2025 Full-Time Orientation
Date: Monday, 06 January – Friday, 17 January 2025
Schools Involved: School of Business, School of Social Health and Sciences, School of Science and Technology, English Language Preparatory Program, Pre-University Foundation Programs, Study Abroad
Key Events & Schedule:
Welcome Session
Time: 09:00 AM – 09:10 AM
Venue: Block C
Dress Code: Smart Casual (No shorts or slippers)
Medical Check-Up & Student’s Pass Formalities (For International Students)
Date: 06 – 07 January 2025
Time: 09:00 AM – 03:00 PM (Last registration at 02:00 PM)
Venue: Block C
Required Documents: Passport, IPA Letter
Welcome Speech & JCU 101 (For ALL Students)
Date: 16 January 2025
Time: 09:00 AM – 09:10 AM
Speakers: Deputy Vice-Chancellor, Acting Campus Dean & Head of Learning, Teaching & Student Engagement
DigiLearn Workshop & Academic Advising
Date: 16 January 2025
Time: 09:10 AM – 10:25 AM
Venue: Block C
Note: Students must complete JCU GetStarted before attending
Explore Booths (For ALL Students)
Departments: Academic support, career services, student well-being, campus life
Partners: Accommodation & Telecommunication Services
Welcome Bags & JCU T-shirts: Available from 07 January – 20 February 2025
Breakout Sessions for Academic Advising
Date: 16 January 2025
Time: 10:40 AM – 11:40 AM
Courses Covered: Business, Environmental Science, IT, Psychology, Pre-University Programs
Networking with Lecturers & Peers
Date: 16 January 2025
Time: 01:30 PM – 03:00 PM
Venue: Block E
Note: Afternoon tea provided
Student’s Pass Completion Formalities (Compulsory for International Students)
Date: 16 January 2025
Time: 03:00 PM – 05:00 PM
Venue: Multi-Purpose Hall
Campus & Singapore Exploration
Date: 14 January 2025
Time: 02:00 PM – 05:30 PM
Venue: James Cook University → The Shoppes Marina Bay Sands
Activities: Campus tour, fun activities"""}]

response = ollama.chat(model=model, messages=messages)

print("Hi, How can i help you?")

question = input(">")
while question != "":
    messages.append({'role': 'user', 'content': question})
    response = ollama.chat(model=model, messages=messages)
    messages.append({'role': 'assistant', 'content': response.message.content})
    print(response.message.content)
    question = input(">")
