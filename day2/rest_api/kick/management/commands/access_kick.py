from django.core.management.base import BaseCommand
from django.utils import timezone
import csv
from kick.models import KickstarterTypes

class Command(BaseCommand):
    help = 'Access certain elements'

    def add_arguments(self, parser):
        parser.add_argument('user_id', nargs='+', type=int, help='User ID')
    
    def handle(self, *args, **kwargs):
        KickstarterTypes.objects.all().delete()
        with open("kick/data/Kickstarter.csv") as csv_file:
            csv_reader = csv.reader(csv_file,delimiter=",")
            #rows = [row for row in csv_reader]
            cur_row = 0
            for row in csv_reader:
                if cur_row != 0:
                    KickstarterTypes.objects.create(backers_count = row[0],
                                                    blurb = row[1],
                    )
                    '''
                                                    category = row[2],
                                                    converted_pledged_amount = row[3],
                                                    country = row[4],
                                                    created_at = row[5],
                                                    creator = row[6],
                                                    currency = row[7],
                                                    deadline=row[8],
                                                    disable_communication=row[9],
                                                    fx_rate=row[10],
                                                    goal=row[11],
                                                    kickstarter_id=row[12],
                                                    launched_at=row[13],
                                                    location=row[14],
                                                    name=row[15],
                                                    photo=row[16],
                                                    pledged=row[17],
                                                    profile=row[18],
                                                    slug=row[19],
                                                    source_url=row[20],
                                                    spotlight=row[21],
                                                    staff_pick=row[22],
                                                    state=row[23],
                                                    state_changed_at=row[24],
                                                    static_usd_rate=row[25],
                                                    urls=row[26],
                                                    usd_pledged=row[27],
                                                    usd_type=row[28],
                   '''

                cur_row += 1
                '''
                print(kwargs['user_id'][0])
                user_num = kwargs['user_id'][0]
                print(KickstarterTypes.objects.get(id=user_num))
                '''
            

                
