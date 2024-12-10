import animals_web_generator

with open('animals_template.html',"r")as file:
  page = file.read()

print(page)
new_html=page.replace("__REPLACE_ANIMALS_INFO__", animals_web_generator.output)
print(new_html)

with open ("animals.html", "w") as file:
  file.write(page.replace("__REPLACE_ANIMALS_INFO__", animals_web_generator.output))