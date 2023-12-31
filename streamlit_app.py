import streamlit
import pandas
import snowflake.connector
import requests
from urllib.error import URLError

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#create repeatable code aka function
def get_fruityvice_data(fruit_choice_)

#new fruityvice section
streamlit.header("Fruityvice Fruit Advice!')
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
    fruityvice_response = requests.get('https://fruityvice.com/api/fruit/' + fruit_choice)
    fruityvice_normalize = pandas.json_normalize(fruityvice_response.json())

  except URLErorr as e:
    stramlit.error()

#Import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
my_data_rows = my_cur.fetchall()
#streamlit.header("The fruit load list contains:")
#streamlit.dataframe(my_data_rows)

add_my_fruit = streamlit.text_input("What fruit would you like to add?")
add_my_fruit = streamlit.write("Thank you for adding ", add_my_fruit)

#import requests
my_cur.execute("insert into pc_rivery_db.public.fruit_load_list values ('from streamlit')")

