from django.contrib import admin
from .models import Quiz, Question, QuizAttempt


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "topic",
        "created_by",
        "is_published",
        "created_at",
    )

    list_filter = ("is_published", "topic")
    search_fields = ("title",)

    inlines = [QuestionInline]

    readonly_fields = ("created_by",)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)


@admin.register(QuizAttempt)
class QuizAttemptAdmin(admin.ModelAdmin):
    list_display = (
        "quiz",
        "student",
        "score",
        "total_marks",
        "attempted_at",
    )

    list_filter = ("quiz",)
