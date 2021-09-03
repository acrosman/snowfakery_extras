"""Provider for Faker which adds fake higher ed info"""

from faker import Faker
from faker.generator import Generator
import faker.providers.address.en_US
import faker.providers.lorem.en_US

fake = Faker()
fakeAddress = faker.providers.address.en_US.Provider(Generator())
fakeLorem = faker.providers.lorem.en_US.Provider(Generator())

INSTITUTIONTYPES = {
    'University',
    'College',
    'Junior College'
}

TOPICS = {
    set(fakeAddress.states).add(fakeLorem.word_list)
}


class Provider(faker.providers.BaseProvider):
    def institution_name(self):
        """Fake higher ed names."""
        suffix = self.random_element(INSTITUTIONTYPES)
        topic = self.random_element(TOPICS)
        return " ".join([topic, suffix]).strip()
        
