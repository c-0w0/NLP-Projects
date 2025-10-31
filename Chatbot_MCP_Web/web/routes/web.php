<?php

use App\Http\Controllers\ChatController;
use Illuminate\Support\Facades\Route;

Route::get('/', [ChatController::class, 'showChat']);
Route::post('/send-message', [ChatController::class, 'sendMessage']);