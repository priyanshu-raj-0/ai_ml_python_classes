
# Defining a class

class Dog:
    def __init__(self, name, bread):    # Dunder method
        self.name = name
        self.bread = bread

    def eat(self):
        print(f"{self.name} is eating")
    
    def shit(self):
        print(f"{self.name} has shitten")


dog_1 = Dog("Buddy", "Golden Retriever")
dog_1.shit()
dog_1.eat()
dog_1.name
dog_1.bread

dog2 = Dog("Bunny","Lebrador")
dog2.shit()
dog2.eat()
print(f"{dog2.name} is a {dog2.bread}")


# ---------------------------------------------------------------------

# real world example
class APIConfig:
    def __init__(self, api_key, model="gpt-3.5-turbo", max_tokens=100):
        self.api_key = api_key
        self.model = model
        self.max_tokens = max_tokens
        self.base_url = "https://api.openai.com/v1"


# Create different configurations
# Using positional for required arg, named for optional
dev_config = APIConfig("sk-dev-key", max_tokens=50)

# Using all named arguments (clearest)
prod_config = APIConfig(api_key="sk-dev-key", model="gpt-4", max_tokens=1000)


print(dev_config.model)
print(prod_config.model)
print(prod_config.max_tokens)


# APIConfig is the class
# config1 and config2 are instances
config1 = APIConfig(api_key="key1", max_tokens=50)
config2 = APIConfig(api_key="key2", max_tokens=200)

# Each instance has its own data
print(config1.max_tokens)  # 50
print(config2.max_tokens)  # 200

# Changing one doesn't affect the other
config1.max_tokens = 75
print(config1.max_tokens)  # 75
print(config2.max_tokens)  # 200 (unchanged)


class APIClient:
    version = "1.0"              # Same for all clients
    max_retries = 3              # Same for all clients

    def __init__(self, api_key, base_url):
        self.api_key = api_key      # Each client has its own key
        self.base_url = base_url    # Each client has its own URL
        self.request_count = 0      # Track requests per client


# Creating instances with named arguments
client1 = APIClient(api_key="key1", base_url="https://api1.com")
client2 = APIClient(api_key="key2", base_url="https://api2.com")



#-------------------------------------------------------------------------------------

# Data validator

class DataValidator:
    def __init__(self):
        self.errors = []
    
    def validate_email(self, email):
        if "@" not in email:
            self.errors.append(f"Invalid email : {email}")
            return False
        return True
    

    def validate_age(self, age):
        if age < 0 or 150 < age :
            self.errors.append(f"Invalid age : {age}")
            return False
        return True
    
    def get_errors(self):
        return self.errors
    

validator = DataValidator()
validator.validate_email("priyanshurajgmail.com")
validator.validate_age(123)
validator.validate_email("Priyanshuraj@gmail.com")
validator.validate_age(155)
print(validator.get_errors())



# -------------------------------------------------------------------------------------------------

# Inheritance in oops

class animal :
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def eat(self):
        return f"{self.name} is eating."

    def sleep(self):
        return f"{self.name} is sleeping."
    

class horse(animal):
    def __init__(self,name, age, bread):
        super().__init__(name, age)
        self.bread = bread

    def sound(self):
        return f"{self.name} says hehee.."
    

monkesh = animal("monkesh", 4)

horesh = horse("horesh", 5, "montain bread")

print(monkesh.name)
print(monkesh.age)
print(horesh.sound())
print(monkesh.sleep())
print(horesh.sleep())
print(horesh.eat())



# --------------------------------------------------------------------------------------
class Animal:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        return f"{self.name} makes a sound"

class Dog(Animal):
    def make_sound(self):  # Override parent method
        return f"{self.name} barks: Woof!"

class Cat(Animal):
    def make_sound(self):  # Override parent method
        return f"{self.name} meows: Meow!"

# Different animals, different sounds
generic = Animal(name="Something")
dog = Dog(name="Buddy")
cat = Cat(name="Whiskers")

print(generic.make_sound())  # Something makes a sound
print(dog.make_sound())      # Buddy barks: Woof!
print(cat.make_sound())      # Whiskers meows: Meow!





# ------------------------------------------------------------------------------

class BaseModel:
    def __init__(self, model_name):
        self.model_name = model_name
        self.is_loaded = False
    
    def load(self):
        print(f"Loading {self.model_name}")
        self.is_loaded = True

class TextModel(BaseModel):
    def __init__(self, model_name, max_length=1000):
        super().__init__(model_name)
        self.max_length = max_length

    
    def process_text(self, text):
        if not self.is_loaded:
            self.load()
        
        if len(text) > self.max_length:
            self.text = text[:self.max_length]
            return f"Processed Text : {self.text}"


newBaseModel = BaseModel("gpt-3.5-turbo")
newBaseModel.load()

newTextModel = TextModel(newBaseModel.model_name, 10)

processtxt = newTextModel.process_text("hello my name is priyanshu raj and i am good.")
print(processtxt)



#---------------------------------------------------------------------------------------------

# Difference between using function and classes


# Here we are using function
def clean_text(text):
    return text.strip().lower()

def remove_punctuation(text):
    return text.replace(".", "").replace(",","")


result = clean_text(remove_punctuation("      Hello, world..     "))
print(result)



# Here we are using classes

class TextProcessor:
    def __init__(self, text):
        self.text = text

    def clean_text(self):
        self.text = self.text.strip().lower()
        return self     # returning class object

    def remove_punctuation(self):
        self.text = self.text.replace(",","").replace(".","")
        return self     # returning class object

TextToBeProcessed = TextProcessor("      Hello, world..     ")
result = TextToBeProcessed.clean_text().remove_punctuation().text

# OR
# result = TextToBeProcessed.clean_text().remove_punctuation()
# result.text











