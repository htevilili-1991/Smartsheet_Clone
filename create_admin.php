<?php

use App\Models\User;

User::create([
    'name' => 'Herman Tevilili',
    'email' => 'htevilili@vanuatu.gov.vu',
    'password' => bcrypt('password'),
]);
