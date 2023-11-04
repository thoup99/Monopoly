import pygame

class Input:
    subscribers = {
        pygame.KEYDOWN: [],
        pygame.KEYUP: [],
        pygame.QUIT: [],
        pygame.MOUSEMOTION: [],
        pygame.MOUSEBUTTONDOWN: []
    }

    def get_inputs():
        for event in pygame.event.get():
            if event.type in Input.subscribers:
                Input.publish(event)

    def subscribe(event: pygame.event.Event.type, callback):
        Input.subscribers[event].append(callback)

    def unsubscribe(event: pygame.event.Event.type, callback):
        Input.subscribers[event].pop(callback)

    def publish(event: pygame.event.Event):
        for callback in Input.subscribers[event.type]:
            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                callback(event.key)
                
            if event.type == pygame.QUIT:
                callback()