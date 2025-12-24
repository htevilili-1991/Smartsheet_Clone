<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;
use App\Http\Controllers\Auth\AuthController;

Route::post('/login', [AuthController::class, 'login']);

Route::middleware('auth:sanctum')->group(function () {
    Route::post('/register', [AuthController::class, 'register'])->middleware('role:admin');
    Route::post('/logout', [AuthController::class, 'logout']);
    Route::get('/me', [AuthController::class, 'me']);

    // Example of a route protected by a role
    Route::get('/admin/projects', function () {
        return 'This is a list of projects for admins';
    })->middleware('role:admin');

    // Example of a route protected by a permission
    Route::get('/projects', function () {
        return 'This is a list of projects';
    })->middleware('permission:view_project');
});
