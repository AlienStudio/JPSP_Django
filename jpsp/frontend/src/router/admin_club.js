import Vue from 'vue'
import Router from 'vue-router'
import index from '@/pages/admin_club/index'
import PostEdit from '@/pages/admin_club/PostEdit'
import ProfileEdit from '@/pages/admin_club/ProfileEdit'
import ClubPageSettings from '@/pages/admin_club/ClubPageSettings'
import MemberManagement from '@/pages/admin_club/MemberManagement'
import RecruitClassroomEdit from '@/pages/admin_club/RecruitClassroomEdit'
import RecruitMember from '@/pages/admin_club/RecruitMember.vue'
import About from '@/pages/public/About.vue'
import Contact from '@/pages/public/Contact.vue'
import Establish from '@/pages/admin_club/Establish.vue'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Index',
      component: index
    },
    {
      path: '/post',
      name: 'Post',
      component: PostEdit
    },
    {
      path: '/profile',
      name: 'Profile',
      component: ProfileEdit
    },
    {
      path: '/establish',
      name: 'Establish',
      component: Establish
    },
    {
      path: '/page',
      name: 'ClubPageSettings',
      component: ClubPageSettings
    },
    {
      path: '/recruit',
      name: 'Recruit',
      component: RecruitClassroomEdit,
      children: [
        {
          path: 'classroom',
          name: 'RecruitClassroomApply',
          component: RecruitClassroomEdit
        },
        {
          path: 'member',
          name: 'RecruitMember',
          component: RecruitMember
        }
      ]
    },
    {
      path: '/member',
      name: 'Member',
      component: MemberManagement
    },
    {
      path: '/about',
      name: 'About',
      component: About
    },
    {
      path: '/contact',
      name: 'Contact',
      component: Contact
    }
  ]
})
