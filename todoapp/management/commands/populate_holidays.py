from django.core.management.base import BaseCommand
from todoapp.models import IndianHoliday
from datetime import date

class Command(BaseCommand):
    help = 'Populate Indian holidays for 2025 and 2026'

    def handle(self, *args, **kwargs):
        # Clear existing holidays
        IndianHoliday.objects.all().delete()
        
        # Indian holidays for 2025
        holidays_2025 = [
            # National Holidays
            ('Republic Day', date(2025, 1, 26), 'Republic Day of India', True),
            ('Independence Day', date(2025, 8, 15), 'Independence Day of India', True),
            ('Gandhi Jayanti', date(2025, 10, 2), 'Birthday of Mahatma Gandhi', True),
            
            # Religious and Cultural Holidays
            ('New Year', date(2025, 1, 1), 'New Year\'s Day', False),
            ('Makar Sankranti', date(2025, 1, 14), 'Harvest festival', False),
            ('Maha Shivaratri', date(2025, 2, 26), 'Festival dedicated to Lord Shiva', False),
            ('Holi', date(2025, 3, 14), 'Festival of Colors', False),
            ('Ram Navami', date(2025, 4, 6), 'Birthday of Lord Rama', False),
            ('Mahavir Jayanti', date(2025, 4, 10), 'Birthday of Lord Mahavira', False),
            ('Good Friday', date(2025, 4, 18), 'Christian holiday', False),
            ('Buddha Purnima', date(2025, 5, 12), 'Birthday of Gautama Buddha', False),
            ('Eid ul-Fitr', date(2025, 3, 31), 'Islamic festival', False),
            ('Eid ul-Adha', date(2025, 6, 7), 'Islamic festival of sacrifice', False),
            ('Muharram', date(2025, 7, 6), 'Islamic New Year', False),
            ('Raksha Bandhan', date(2025, 8, 9), 'Festival celebrating brother-sister bond', False),
            ('Krishna Janmashtami', date(2025, 8, 16), 'Birthday of Lord Krishna', False),
            ('Ganesh Chaturthi', date(2025, 8, 27), 'Festival of Lord Ganesha', False),
            ('Dussehra', date(2025, 10, 2), 'Victory of good over evil', False),
            ('Diwali', date(2025, 10, 20), 'Festival of Lights', False),
            ('Guru Nanak Jayanti', date(2025, 11, 5), 'Birthday of Guru Nanak', False),
            ('Christmas', date(2025, 12, 25), 'Birthday of Jesus Christ', False),
        ]
        
        # Indian holidays for 2026
        holidays_2026 = [
            # National Holidays
            ('Republic Day', date(2026, 1, 26), 'Republic Day of India', True),
            ('Independence Day', date(2026, 8, 15), 'Independence Day of India', True),
            ('Gandhi Jayanti', date(2026, 10, 2), 'Birthday of Mahatma Gandhi', True),
            
            # Religious and Cultural Holidays
            ('New Year', date(2026, 1, 1), 'New Year\'s Day', False),
            ('Makar Sankranti', date(2026, 1, 14), 'Harvest festival', False),
            ('Maha Shivaratri', date(2026, 3, 17), 'Festival dedicated to Lord Shiva', False),
            ('Holi', date(2026, 3, 25), 'Festival of Colors', False),
            ('Ram Navami', date(2026, 4, 21), 'Birthday of Lord Rama', False),
            ('Mahavir Jayanti', date(2026, 4, 2), 'Birthday of Lord Mahavira', False),
            ('Good Friday', date(2026, 4, 3), 'Christian holiday', False),
            ('Buddha Purnima', date(2026, 5, 1), 'Birthday of Gautama Buddha', False),
            ('Eid ul-Fitr', date(2026, 3, 20), 'Islamic festival', False),
            ('Eid ul-Adha', date(2026, 5, 28), 'Islamic festival of sacrifice', False),
            ('Muharram', date(2026, 6, 25), 'Islamic New Year', False),
            ('Raksha Bandhan', date(2026, 8, 28), 'Festival celebrating brother-sister bond', False),
            ('Krishna Janmashtami', date(2026, 9, 4), 'Birthday of Lord Krishna', False),
            ('Ganesh Chaturthi', date(2026, 9, 15), 'Festival of Lord Ganesha', False),
            ('Dussehra', date(2026, 10, 21), 'Victory of good over evil', False),
            ('Diwali', date(2026, 11, 8), 'Festival of Lights', False),
            ('Guru Nanak Jayanti', date(2026, 11, 24), 'Birthday of Guru Nanak', False),
            ('Christmas', date(2026, 12, 25), 'Birthday of Jesus Christ', False),
        ]
        
        # Create holidays
        for name, date_obj, description, is_national in holidays_2025 + holidays_2026:
            IndianHoliday.objects.create(
                name=name,
                date=date_obj,
                description=description,
                is_national=is_national,
                year=date_obj.year
            )
        
        self.stdout.write(self.style.SUCCESS('Successfully populated Indian holidays for 2025 and 2026'))
