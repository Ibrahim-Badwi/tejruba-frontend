<template>
<div class="toolbar">
    <div class="gradient"></div>
    <v-toolbar app dark color="primary">
        <v-layout row align-center justify-space-between>

            <!-- logo -->
            <img src="../../assets/img/T_logo.svg" class="ml-3 " height="25px" />
            <!-- pageName -->
            <span class="center pr-2 white--text">
                {{ currentPage }}
            </span>
            <!-- Avatar -->
            <v-avatar size="33" color="primary" >
                <img   :src="userAvatar || 'http://s3.amazonaws.com/37assets/svn/765-default-avatar.png'"
                    alt="avatar">
            </v-avatar>

        </v-layout>
    </v-toolbar>
</div>
   
</template>

<script>
    export default {
        data(){
            return{
            }
        },
        computed: {
            currentPage() {
                return this.$store.state.currentPage
            },
            userAvatar(){
              return this.$store.getters.userInfo.avatar 
            }
        }
    }
</script>

<style lang="scss" scoped>
    @import '../../styles/components/app-layout/Header';
</style>