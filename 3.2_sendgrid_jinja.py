# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import jinja2

import pandas as pd

def render_template(template, **kwargs):
    ''' renders a Jinja template into HTML '''
    # check if template exists
    if not os.path.exists(template):
        print('No template file present: %s' % template)
        sys.exit()

    dummy_data = {1: {'url': 'https://jerseydigs.com/bayonne-to-suspend-affordable-housing-requirements-for-1500-unit-development/', 'author': 'Jared Kofsky', 'title': 'Bayonne Could ‘Suspend Affordable Housing Requirements’ for 1,500+ Unit Development', 'date': 'Wed, 19 Jun 2019 13:30:02 +0000', 'summary': '<p>Jersey Digs has exclusively learned new details about a massive proposed high-rise development with seven buildings at the MOTBY site in Bayonne.</p>\n<p>The post <a rel="nofollow" href="https://jerseydigs.com/bayonne-to-suspend-affordable-housing-requirements-for-1500-unit-development/">Bayonne Could ‘Suspend Affordable Housing Requirements’ for 1,500+ Unit Development</a> appeared first on <a rel="nofollow" href="https://jerseydigs.com">Jersey Digs</a>.</p>', 'tags': ['Bayonne', 'Development', 'Politics', 'Malakshmi Goldsborough', 'Military Ocean Terminal']}, 2: {'url': 'https://jerseydigs.com/brooklyn-caffe-buon-gusto-opening-hoboken-location/', 'author': 'Chris Fry', 'title': 'Brooklyn’s Caffe Buon Gusto Opening Hoboken Location', 'date': 'Wed, 19 Jun 2019 13:00:31 +0000', 'summary': '<p>A pasta-centric Italian restaurant known for their cozy candlelit spaces is expanding across the Hudson River into the Mile Square City. </p>\n<p>The post <a rel="nofollow" href="https://jerseydigs.com/brooklyn-caffe-buon-gusto-opening-hoboken-location/">Brooklyn’s Caffe Buon Gusto Opening Hoboken Location</a> appeared first on <a rel="nofollow" href="https://jerseydigs.com">Jersey Digs</a>.</p>', 'tags': ['Food & Drink', 'Hoboken', '918 Washinton Street', 'caffe buon gusto']}, 3: {'url': 'https://jerseydigs.com/244-2nd-198-morgan-street-jersey-city-sold-5-3m/', 'author': 'Mario Marroquin', 'title': '14 Units Near Grove Street PATH in Jersey City Fetch $5.3M', 'date': 'Wed, 19 Jun 2019 12:30:25 +0000', 'summary': '<p>Two properties at 244 2nd Street and 198 Morgan Street traded to two international funds, brokerage firm Marcus &#038; Millichap announced.</p>\n<p>The post <a rel="nofollow" href="https://jerseydigs.com/244-2nd-198-morgan-street-jersey-city-sold-5-3m/">14 Units Near Grove Street PATH in Jersey City Fetch $5.3M</a> appeared first on <a rel="nofollow" href="https://jerseydigs.com">Jersey Digs</a>.</p>', 'tags': ['Deal', 'Jersey City', '198 Morgan Street', '244 2nd Street', 'downtown']}, 4: {'url': 'https://jerseydigs.com/peek-inside-cafe-peanut-opens-586-newark-ave-journal-square-jersey-city/', 'author': 'Chris Fry', 'title': 'A Peek Inside Café Peanut, Opening Today Near Journal Square', 'date': 'Tue, 18 Jun 2019 13:30:45 +0000', 'summary': '<p>Newark Avenue’s self-described “funky little place” will finally start serving customers their artisanal coffee and teas, salads, sandwiches and much more.</p>\n<p>The post <a rel="nofollow" href="https://jerseydigs.com/peek-inside-cafe-peanut-opens-586-newark-ave-journal-square-jersey-city/">A Peek Inside Café Peanut, Opening Today Near Journal Square</a> appeared first on <a rel="nofollow" href="https://jerseydigs.com">Jersey Digs</a>.</p>', 'tags': ['Food & Drink', 'Jersey City', 'Cafe Peanut', 'journal square']}, 5: {'url': 'https://jerseydigs.com/development-proposed-610-612-bloomfield-ave-bloomfield-new-jersey/', 'author': 'Jared Kofsky', 'title': 'New Development Could Rise Up to Eight Stories Over Bloomfield', 'date': 'Tue, 18 Jun 2019 13:00:51 +0000', 'summary': '<p>Bloomfield’s downtown has seen plenty of development over the last decade. Now, another new complex could bring over 200 apartments and stores to the Essex County community.</p>\n<p>The post <a rel="nofollow" href="https://jerseydigs.com/development-proposed-610-612-bloomfield-ave-bloomfield-new-jersey/">New Development Could Rise Up to Eight Stories Over Bloomfield</a> appeared first on <a rel="nofollow" href="https://jerseydigs.com">Jersey Digs</a>.</p>', 'tags': ['Bloomfield', 'Development', '18 Ward St', '610-612 Bloomfield Ave', '81-85 Washington St']}, 6: {'url': 'https://jerseydigs.com/development-plans-underway-weehawken-waterfront-park-lots/', 'author': 'Jared Kofsky', 'title': 'Plans Underway for One of Weehawken’s Last Undeveloped Waterfront Lots', 'date': 'Tue, 18 Jun 2019 12:30:41 +0000', 'summary': '<p>A proposal to bring 300 apartments and a parking garage near Weehawken Waterfront Park could go before the Weehawken Planning Board this week.</p>\n<p>The post <a rel="nofollow" href="https://jerseydigs.com/development-plans-underway-weehawken-waterfront-park-lots/">Plans Underway for One of Weehawken&#8217;s Last Undeveloped Waterfront Lots</a> appeared first on <a rel="nofollow" href="https://jerseydigs.com">Jersey Digs</a>.</p>', 'tags': ['Development', 'Port Imperial', 'Weehawken', 'Mack-Cali', 'waterfront park']}, 7: {'url': 'https://jerseydigs.com/50-story-towers-bates-street-redevelopment-area-jersey-city/', 'author': 'Chris Fry', 'title': 'Four Towers, 2,360 Units Proposed for the Edge of Downtown Jersey City', 'date': 'Mon, 17 Jun 2019 13:46:30 +0000', 'summary': '<p>Still in the early conceptual phase, the massive project would transform one of downtown Jersey City\'s last remaining industrial sections. In order to build it, the developer is ready to provide huge givebacks to the community. </p>\n<p>The post <a rel="nofollow" href="https://jerseydigs.com/50-story-towers-bates-street-redevelopment-area-jersey-city/">Four Towers, 2,360 Units Proposed for the Edge of Downtown Jersey City</a> appeared first on <a rel="nofollow" href="https://jerseydigs.com">Jersey Digs</a>.</p>', 'tags': ['Development', 'Infrastructure', 'Jersey City', 'Proposal', 'Bates Street Redevelopment Area', 'downtown', 'jc', 'Manhattan Building Company']}, 8: {'url': 'https://jerseydigs.com/enclave-apartments-open-jersey-city/', 'author': 'Darrell Simmons', 'title': 'Development Team, Jersey City Mayor Steven Fulop Officially Open The Enclave', 'date': 'Mon, 17 Jun 2019 13:45:49 +0000', 'summary': '<p>Recently, the development team hosted Jersey City Mayor Steven Fulop for a ceremonial ribbon cutting to officially open the new property.</p>\n<p>The post <a rel="nofollow" href="https://jerseydigs.com/enclave-apartments-open-jersey-city/">Development Team, Jersey City Mayor Steven Fulop Officially Open The Enclave</a> appeared first on <a rel="nofollow" href="https://jerseydigs.com">Jersey Digs</a>.</p>', 'tags': ['Development', 'Event', 'Jersey City', 'Lackawanna', 'soho west', 'The Enclave', 'van leer place']}, 9: {'url': 'https://jerseydigs.com/development-254-270-orange-ave-newark-proposed-gomes-group/', 'author': 'Jared Kofsky', 'title': 'Gomes Group Plans Over 100 Units in Newark’s Central Ward', 'date': 'Mon, 17 Jun 2019 13:30:06 +0000', 'summary': '<p>A plan to bring 105 apartments and retail space not far from the Newark Broad Street Station could soon be approved.</p>\n<p>The post <a rel="nofollow" href="https://jerseydigs.com/development-254-270-orange-ave-newark-proposed-gomes-group/">Gomes Group Plans Over 100 Units in Newark’s Central Ward</a> appeared first on <a rel="nofollow" href="https://jerseydigs.com">Jersey Digs</a>.</p>', 'tags': ['Development', 'Newark', 'Gomes & Gomes', 'gomes group']}, 10: {'url': 'https://jerseydigs.com/cherry-hill-contemporary-1146a-barbara-drive-for-sale/', 'author': 'Rima Abousleiman', 'title': 'This 1970s Contemporary in Cherry Hill is a Work of Art', 'date': 'Mon, 17 Jun 2019 13:00:16 +0000', 'summary': '<p>Though in need of some updates, this home offers jaw-dropping architecture in a private location. </p>\n<p>The post <a rel="nofollow" href="https://jerseydigs.com/cherry-hill-contemporary-1146a-barbara-drive-for-sale/">This 1970s Contemporary in Cherry Hill is a Work of Art</a> appeared first on <a rel="nofollow" href="https://jerseydigs.com">Jersey Digs</a>.</p>', 'tags': ['Cherry Hill', 'Listing', '1146A Barbara Drive', 'contemporary', 'modern']}}

    templateLoader = jinja2.FileSystemLoader(searchpath="./")
    templateEnv = jinja2.Environment(loader=templateLoader)
    templ = templateEnv.get_template(template)
    return templ.render(
        feed=dummy_data,
        agent_email=kwargs['agent']
    )

df = pd.read_csv('agents_data_19June2019.csv')

errors = []
for index, row in df.iterrows():

    x = render_template('templates/template.html', agent=row['agent_email'])

    message = Mail(
        to_emails=row['contact_email'],
        from_email=row['agent_email'],
        subject='Weekly Real Estate Feed - June 19, 2019',
        html_content=x)

    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)
        errors.append('{}_{}'.format(row['agent_email'], row['contact_email']))

print(errors)
