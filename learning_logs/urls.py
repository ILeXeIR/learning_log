#Определяет схемы URL для learning_logs.

from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
	#Домашняя страница
	path('', views.index, name='index'),
	#Страница со списком своих тем.
	path('topics/', views.topics, name='topics'),
	#Страница со списом публичных тем.
	path('public_topics/', views.public_topics, name='public_topics'),
	#Страница с подробной информацией по отдельной теме
	path('topics/<int:topic_id>/', views.topic, name='topic'),
	#Страница для добавления новой темы
	path('new_topic/', views.new_topic, name='new_topic'),
	#Страница для добавления новой записи
	path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
	#Страница для редактирования темы
	path('edit_topic/<int:topic_id>/', views.edit_topic, name='edit_topic'),
	#Страница для редактирования записей
	path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
	#Удаление записи
	path('edit_entry/<int:entry_id>/delete/', views.delete_entry, name='delete_entry'),
	#Удаление темы
	path('topics/<int:topic_id>/delete/', views.delete_topic, name='delete_topic'),
]
