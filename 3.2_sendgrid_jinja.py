# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import jinja2

def render_template(template, **kwargs):
    ''' renders a Jinja template into HTML '''
    # check if template exists
    if not os.path.exists(template):
        print('No template file present: %s' % template)
        sys.exit()


    dummy_data = {1: {'author': 'Rima Abousleiman',
     'date': 'Thu, 23 May 2019 13:30:32 +0000',
     'summary': '<p>This award-winning "all grown up" treehouse in Mountain '
                'Lakes is a modern marvel of engineering. </p>\n'
                '<p>The post <a rel="nofollow" '
                'href="https://jerseydigs.com/mid-century-modern-treehouse-for-sale-9-van-duyne-road-mountain-lakes/">Live '
                'Amongst the Birds in This Unusual Mid-Century Modern '
                'Treehouse</a> appeared first on <a rel="nofollow" '
                'href="https://jerseydigs.com">Jersey Digs</a>.</p>',
     'tags': ['Listing', 'Mountain Lakes', '9 Van Duyne Road'],
     'title': 'Live Amongst the Birds in This Unusual Mid-Century Modern '
              'Treehouse',
     'url': 'https://jerseydigs.com/mid-century-modern-treehouse-for-sale-9-van-duyne-road-mountain-lakes/'},
 2: {'author': 'Gillian Blair',
     'date': 'Thu, 23 May 2019 13:00:39 +0000',
     'summary': '<p>Through trusted partnerships with local New Jersey '
                'sustainable farms, Bone-In offers a hearty organic selection '
                'and next-day delivery to Jersey City, Hoboken, and '
                'beyond.</p>\n'
                '<p>The post <a rel="nofollow" '
                'href="https://jerseydigs.com/bone-in-local-organic-food-delivery-sustainable-farms-new-jersey/">Meet '
                'Bone-In, the Company Delivering NJ Farms to Your Front '
                'Door</a> appeared first on <a rel="nofollow" '
                'href="https://jerseydigs.com">Jersey Digs</a>.</p>',
     'tags': ['Business Profile',
              'Food & Drink',
              'Local Spotlight',
              'New Jersey',
              'Bone-In'],
     'title': 'Meet Bone-In, the Company Delivering NJ Farms to Your Front '
              'Door',
     'url': 'https://jerseydigs.com/bone-in-local-organic-food-delivery-sustainable-farms-new-jersey/'},
 3: {'author': 'Jared Kofsky',
     'date': 'Thu, 23 May 2019 12:30:23 +0000',
     'summary': '<p>Plans to construct a 420-unit apartment complex on a '
                'currently undeveloped 21-acre tract between Princeton and '
                'Hightstown could possibly be approved tonight.</p>\n'
                '<p>The post <a rel="nofollow" '
                'href="https://jerseydigs.com/village-center-mixed-use-affordable-complex-proposed-west-windsor/">Village '
                'Center Complex Could Bring 420 &#8216;Affordable&#8217; Units '
                'to West Windsor</a> appeared first on <a rel="nofollow" '
                'href="https://jerseydigs.com">Jersey Digs</a>.</p>',
     'tags': ['Development', 'West Windsor', 'Village Center'],
     'title': 'Village Center Complex Could Bring 420 ‘Affordable’ Units to '
              'West Windsor',
     'url': 'https://jerseydigs.com/village-center-mixed-use-affordable-complex-proposed-west-windsor/'},
 4: {'author': 'Gillian Blair',
     'date': 'Wed, 22 May 2019 13:30:11 +0000',
     'summary': '<p>1425 Hudson Street at Hudson Tea offers luxury condos '
                'complemented by equally luxurious amenities in a prime Uptown '
                'Hoboken location.</p>\n'
                '<p>The post <a rel="nofollow" '
                'href="https://jerseydigs.com/1425-hudson-street-at-hudson-tea-hoboken-luxury-condos-for-sale-rooftop-deck-pool/">Just '
                'in Time for Summer: The Resident Rooftop at 1425 Hudson '
                'Street is a Luxe Indulgence</a> appeared first on <a '
                'rel="nofollow" href="https://jerseydigs.com">Jersey '
                'Digs</a>.</p>',
     'tags': ['Hoboken',
              'Luxury Condos',
              'Sponsored',
              '1425 Hudson Street at Hudson Tea'],
     'title': 'Just in Time for Summer: The Resident Rooftop at 1425 Hudson '
              'Street is a Luxe Indulgence',
     'url': 'https://jerseydigs.com/1425-hudson-street-at-hudson-tea-hoboken-luxury-condos-for-sale-rooftop-deck-pool/'},
 5: {'author': 'Jersey Digs',
     'date': 'Wed, 22 May 2019 13:00:05 +0000',
     'summary': '<p>We recently rode the hoist up to the 79th floor of Jersey '
                'City’s 99 Hudson for a first-hand look at the views from the '
                'pinnacle of New Jersey.</p>\n'
                '<p>The post <a rel="nofollow" '
                'href="https://jerseydigs.com/best-nyc-skyline-views-jersey-city-new-jersey/">The '
                'Best Views of NYC Are in… New Jersey</a> appeared first on <a '
                'rel="nofollow" href="https://jerseydigs.com">Jersey '
                'Digs</a>.</p>',
     'tags': ['Development', 'Jersey City', 'Video', '99 Hudson', 'downtown'],
     'title': 'The Best Views of NYC Are in… New Jersey',
     'url': 'https://jerseydigs.com/best-nyc-skyline-views-jersey-city-new-jersey/'},
 6: {'author': 'Jared Kofsky',
     'date': 'Wed, 22 May 2019 12:30:43 +0000',
     'summary': "<p>Jersey City's Zoning Board will hear a proposal for a new "
                "project that's requesting variances for use and height. </p>\n"
                '<p>The post <a rel="nofollow" '
                'href="https://jerseydigs.com/development-proposed-227-summit-avenue-mcginley-square-jersey-city/">Development '
                'Proposal Calls for 19 Units Near McGinley Square</a> appeared '
                'first on <a rel="nofollow" '
                'href="https://jerseydigs.com">Jersey Digs</a>.</p>',
     'tags': ['Development',
              'Jersey City',
              '227 Summit Avenue',
              'McGinley Square'],
     'title': 'Development Proposal Calls for 19 Units Near McGinley Square',
     'url': 'https://jerseydigs.com/development-proposed-227-summit-avenue-mcginley-square-jersey-city/'},
 7: {'author': 'Gillian Blair',
     'date': 'Tue, 21 May 2019 14:00:01 +0000',
     'summary': '<p>The luxury condos as part of the Port Imperial community '
                'offer residents a wealth of private and public outdoor '
                'amenities along the Hudson River waterfront.</p>\n'
                '<p>The post <a rel="nofollow" '
                'href="https://jerseydigs.com/henley-on-hudson-condos-for-sale-with-outdoor-amenities-port-imperial-weehawken/">Henley '
                'on Hudson Has Summertime Covered on New Jersey’s Gold '
                'Coast</a> appeared first on <a rel="nofollow" '
                'href="https://jerseydigs.com">Jersey Digs</a>.</p>',
     'tags': ['Luxury Condos',
              'Sponsored',
              'Weehawken',
              'featured',
              'Henley on Hudson'],
     'title': 'Henley on Hudson Has Summertime Covered on New Jersey’s Gold '
              'Coast',
     'url': 'https://jerseydigs.com/henley-on-hudson-condos-for-sale-with-outdoor-amenities-port-imperial-weehawken/'},
 8: {'author': 'Rima Abousleiman',
     'date': 'Tue, 21 May 2019 13:30:42 +0000',
     'summary': '<p>Zoned for both commercial and residential use, this '
                'property includes a ground floor retail space and a '
                'loft-style apartment, both boasting a sleek aesthetic. </p>\n'
                '<p>The post <a rel="nofollow" '
                'href="https://jerseydigs.com/live-work-artist-space-21-risler-street-stockton/">Modern, '
                'Lofty Live/Work Space in Stockton Fit for a Maker or '
                'Artist</a> appeared first on <a rel="nofollow" '
                'href="https://jerseydigs.com">Jersey Digs</a>.</p>',
     'tags': ['Listing', 'Stockton', '21 Risler Street'],
     'title': 'Modern, Lofty Live/Work Space in Stockton Fit for a Maker or '
              'Artist',
     'url': 'https://jerseydigs.com/live-work-artist-space-21-risler-street-stockton/'},
 9: {'author': 'Mario Marroquin',
     'date': 'Tue, 21 May 2019 13:00:17 +0000',
     'summary': '<p>Developers BNE Real Estate Group and HornRock Properties '
                'have launched leasing at their luxury community in downtown '
                'Harrison.</p>\n'
                '<p>The post <a rel="nofollow" '
                'href="https://jerseydigs.com/one-harrison-now-leasing-luxury-apartments-for-rent-harrison/">One '
                'Harrison Launches Leasing</a> appeared first on <a '
                'rel="nofollow" href="https://jerseydigs.com">Jersey '
                'Digs</a>.</p>',
     'tags': ['Harrison', 'Luxury Rentals', 'Now Leasing', 'One Harrison'],
     'title': 'One Harrison Launches Leasing',
     'url': 'https://jerseydigs.com/one-harrison-now-leasing-luxury-apartments-for-rent-harrison/'},
 10: {'author': 'Jared Kofsky',
      'date': 'Tue, 21 May 2019 12:30:07 +0000',
      'summary': '<p>If it moves forward, the ambitious Bayonne project within '
                 'the Harbor Station South Redevelopment area would be one of '
                 'the largest developments in New Jersey. </p>\n'
                 '<p>The post <a rel="nofollow" '
                 'href="https://jerseydigs.com/mahalaxmi-harbor-station-south-military-ocean-terminal-bayonne/">New '
                 'Details on Bayonne Mega-Project Include 4500 Units, Hotel, '
                 'Retail</a> appeared first on <a rel="nofollow" '
                 'href="https://jerseydigs.com">Jersey Digs</a>.</p>',
      'tags': ['Bayonne', 'Development', 'bay', 'Military Ocean Terminal'],
      'title': 'New Details on Bayonne Mega-Project Include 4500 Units, Hotel, '
               'Retail',
      'url': 'https://jerseydigs.com/mahalaxmi-harbor-station-south-military-ocean-terminal-bayonne/'}}


    templateLoader = jinja2.FileSystemLoader(searchpath="./")
    templateEnv = jinja2.Environment(loader=templateLoader)
    templ = templateEnv.get_template(template)
    return templ.render(feed=dummy_data)


x = render_template('templates/scratch/template.html')

message = Mail(
    to_emails=['mitchbregs@gmail.com', 'jonathan@fieyomedia.com'],
    from_email='jonathan@fieyomedia.com',
    subject='Weekly Real Estate Feed - June 1, 2019 - Test 15',
    html_content=x)

try:
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)
