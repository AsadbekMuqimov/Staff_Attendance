from django.core.management.base import BaseCommand
from faker import Faker
from .models import Staff, StaffAttendance, Position, Shift, StaffShift
import random
from datetime import datetime, timedelta

fake = Faker()

class Command(BaseCommand):
    help = 'Staff, StaffAttendance, Position, Shift, va StaffShift modellari uchun soxta ma\'lumotlar yaratish'

    def handle(self, *args, **kwargs):
        # Pozitsiyalarni yaratish
        positions = []
        for _ in range(5):  # Talabga ko'ra sonni sozlang
            position = Position.objects.create(name=fake.job())
            positions.append(position)
            self.stdout.write(self.style.SUCCESS(f"Yaratildi: Pozitsiya - {position.name}"))

        # Xodimlarni yaratish
        staff_list = []
        for _ in range(10):  # Talabga ko'ra sonni sozlang
            staff = Staff.objects.create(
                firstname=fake.first_name(),
                surname=fake.last_name(),
            )
            staff_list.append(staff)
            self.stdout.write(self.style.SUCCESS(f"Yaratildi: Xodim - {staff.firstname} {staff.surname}"))

        # Siljishlarni yaratish
        shifts = []
        for _ in range(5):  # Talabga ko'ra sonni sozlang
            start_time = fake.time_object()
            end_time = (datetime.combine(datetime.today(), start_time) + timedelta(hours=random.randint(1, 8))).time()
            shift = Shift.objects.create(
                s_time=start_time,
                e_time=end_time
            )
            shifts.append(shift)
            self.stdout.write(self.style.SUCCESS(f"Yaratildi: Siljish - {shift.s_time} - {shift.e_time}"))

        # Xodimlarning ishtirok yozuvlarini yaratish
        for staff in staff_list:
            for _ in range(3):  # Har bir xodim uchun ishtirok yozuvlari sonini sozlang
                attendance = StaffAttendance.objects.create(
                    staff=staff,
                    s_time=fake.date_time_this_year()
                )
                self.stdout.write(self.style.SUCCESS(f"Yaratildi: Ishtirok - {attendance.s_time} - {staff.firstname} {staff.surname}"))

        # Xodimlarning almashinuvi yozuvlarini yaratish
        for staff in staff_list:
            for _ in range(3):  # Har bir xodim uchun almashinuvi yozuvlari sonini sozlang
                staff_shift = StaffShift.objects.create(
                    staff=staff,
                    shift=random.choice(shifts),
                    start_time=fake.date_time_this_year()
                )
                self.stdout.write(self.style.SUCCESS(f"Yaratildi: Xodim almashinuvi - {staff_shift.staff} - {staff_shift.shift} - {staff_shift.start_time}"))
