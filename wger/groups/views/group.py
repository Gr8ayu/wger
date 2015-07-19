# -*- coding: utf-8 -*-

# This file is part of wger Workout Manager.
#
# wger Workout Manager is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# wger Workout Manager is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy

from django.views.generic import ListView, CreateView, DetailView

from wger.groups.models import Group
from wger.utils.generic_views import WgerPermissionMixin, WgerFormMixin


class ListView(WgerPermissionMixin, ListView):
    '''
    Overview of all available gyms
    '''
    model = Group
    template_name = 'group/list.html'

    def get_queryset(self):
        '''
        List only public groups
        '''
        return Group.objects.filter(public=True)

class AddView(WgerFormMixin, CreateView):
    '''
    View to add a new group
    '''

    # TODO: add user to list of members and make him admin

    model = Group
    fields = ('name',
              'description',
              'image',
              'public')
    title = ugettext_lazy('Create new group')
    form_action = reverse_lazy('groups:group:add')


class DetailView(WgerPermissionMixin, DetailView):
    '''
    Detail view for a group
    '''

    # TODO: check permission/membership
    model = Group
    template_name = 'group/view.html'