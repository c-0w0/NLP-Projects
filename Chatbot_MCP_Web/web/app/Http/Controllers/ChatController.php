<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Http;

class ChatController extends Controller
{
    public function showChat()
    {
        return view('chat');
    }

    public function sendMessage(Request $request)
    {
        $response = Http::post('http://localhost:8001/api/chat', [
            'message' => $request->input('message')
        ]);
        
        return $response->json();
    }
}