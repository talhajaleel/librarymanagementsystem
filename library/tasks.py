from celery import shared_task
from .models import Loan
from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime

@shared_task
def send_loan_notification(loan_id):
    try:
        loan = Loan.objects.get(id=loan_id)
        member_email = loan.member.user.email
        book_title = loan.book.title
        send_mail(
            subject='Book Loaned Successfully',
            message=f'Hello {loan.member.user.username},\n\nYou have successfully loaned "{book_title}".\nPlease return it by the due date.',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[member_email],
            fail_silently=False,
        )
    except Loan.DoesNotExist:
        pass

@shared_task
def check_overdue_loans():
    try:
        now = datetime.now
        all_loan_objs = Loan.objects.filter(
            is_returned=False
        )

        valid_overdue_loans = []

        for loan in all_loan_objs:
            if loan.due_date < now:
                valid_overdue_loans.append(loan)
        
        member_email = loan.member.user.email
        book_title = loan.book.title
        send_mail(
            subject='Book Loan Overdue Notification!',
            message=f'Hello {loan.member.user.username},\n\nYour due date has passed"{book_title}".\nPlease return it.',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[member_email],
            fail_silently=False,
        )

    except Exception:
        pass