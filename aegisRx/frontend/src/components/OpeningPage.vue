<script>
import { RouterLink, RouterView } from 'vue-router'
</script>
<template>
<nav class="bg-sky-900">
  <div class="mx-auto max-w-7xl px-2 sm:px-6 lg:px-8">
    <div class="relative flex h-16 items-center justify-between">
      <div class="absolute inset-y-0 left-0 flex items-center sm:hidden">
        <!-- Mobile menu button-->
        <button type="button" class="relative inline-flex items-center justify-center rounded-md p-2 text-gray-400 hover:bg-gray-700 hover:text-white focus:outline-none focus:ring-2 focus:ring-inset focus:ring-white" aria-controls="mobile-menu" aria-expanded="false">
          <span class="absolute -inset-0.5"></span>
          <span class="sr-only">Open main menu</span>
          <svg class="block h-6 w-6" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true">
            <path stroke-linecap="round" stroke-linejoin="round" d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5" />
          </svg>
          <svg class="hidden h-6 w-6" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true">
            <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
          </svg>
        </button>
      </div>
      <div class="flex flex-1 items-center justify-center sm:items-stretch sm:justify-start">
        <div class="flex flex-shrink-0 items-center">
          <img class="h-12 w-auto" src="/F112D4BE-BD7F-4100-9658-548FBF7FE2B6.png" alt="Aegis">
          <header class="text-gray-300 hover:bg-gray-700 hover:text-white rounded-md px-3 py-2 text-sm font-medium">AegisRx</header>
        </div>
        <div class="hidden sm:ml-12 sm:block">
          <div class="flex space-x-4">
            <!-- Current: "bg-gray-900 text-white", Default: "text-gray-300 hover:bg-gray-700 hover:text-white" -->
            <RouterLink to ="/about" class = "text-gray-300 hover:bg-gray-700 hover:text-white rounded-md px-3 py-2 text-sm font-medium">About Us</RouterLink>
            <RouterLink to = "/" class="text-gray-300 hover:bg-gray-700 hover:text-white rounded-md px-3 py-2 text-sm font-medium">Home</RouterLink>
          </div>
        </div>
      </div>
      <div class="absolute inset-y-0 right-0 flex items-center pr-2 sm:static sm:inset-auto sm:ml-6 sm:pr-0">
        <RouterLink to = "/login" class="bg-gray-900 text-white rounded-md px-3 py-2 text-sm font-medium" aria-current="page">Login</RouterLink>
      </div>
    </div>
  </div>
</nav>
<div class="bg-white dark:bg-gray-800 flex relative z-20 items-center overflow-hidden">
        <div class="container mx-auto px-6 flex relative py-16">
            <div class="sm:w-2/3 lg:w-2/5 flex flex-col relative z-20">
                <span class="w-20 h-2 bg-gray-800 dark:bg-white mb-12">
                </span>
                <h1 class="font-bebas-neue uppercase text-6xl sm:text-8xl font-black flex flex-col leading-none dark:text-white text-gray-800">
                    Be on
                    <span class="text-5xl sm:text-7xl">
                        Time
                    </span>
                </h1>
              </br>
                <header>
                  <ul class="space-y-4 text-gray-500 list-disc list-inside dark:text-white">
                    <li>
                    Research Medications
                  </li>
                  <li>
                    Look up interactions
                  </li>
                  <li>
                    Track and get notified in real time
                  </li>
                  </ul>
                </header>
                <div class="flex mt-8">
                    <RouterLink to = "/login" class="uppercase py-2 px-4 rounded-lg bg-blue-700 border-2 border-transparent text-white text-md mr-4 hover:bg-blue-400">
                        Sign Up
                    </RouterLink>
                    <RouterLink to = "/about" class="uppercase py-2 px-4 rounded-lg bg-transparent border-2 border-blue-700 text-blue-400 dark:text-white hover:bg-blue-400 hover:text-white text-md">
                        Learn More
                    </RouterLink>
                </div>
            </div>
            <div class="hidden sm:block sm:w-1/3 lg:w-3/5 relative">
                <img src="/1098028.png" class="max-w-xs md:max-w-sm m-auto"/>
            </div>
        </div>
    </div>
    <footer class="bg-white dark:bg-gray-900 max-h-full">
      <div class = "w-full max-w-screen-xl mx-auto p-12 md:py-8">
        <RouterLink to = "/" class="flex items-center mb-4 sm:mb-0 space-x-3 rtl:space-x-reverse">
                <img src="/F112D4BE-BD7F-4100-9658-548FBF7FE2B6.png" class="h-8" alt="Aegis Logo" />
                <span class="self-center text-2xl font-semibold whitespace-nowrap dark:text-white">AegisRx</span>
        </RouterLink>
            <ul class="flex flex-wrap items-center mb-6 text-sm font-medium text-gray-500 sm:mb-0 dark:text-gray-400">
                <li>
                    <RouterLink to = "/about" class="hover:underline me-4 md:me-6">About</RouterLink>
                </li>
                <li>
                    <a href="https://github.com/twonkista/MedicationTracker-" class="hover:underline me-4 md:me-6">Github</a>
                </li>
            </ul>
            <hr class="my-6 border-gray-200 sm:mx-auto dark:border-gray-700 lg:my-8" />
        <span class="block text-sm text-gray-500 sm:text-center dark:text-gray-400">© 2019
        <RouterLink to = "/" class="hover:underline">AegisRx</RouterLink><a>. No Rights Reserved.</a></span>
        </div>
    </footer>
</template>