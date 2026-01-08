package com.yash.tixito.controller;


import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/event")
public class EventController {

    @GetMapping("/{eventID}/seats")
    public List<Seat> getEventAvailableSeats(@PathVariable("eventID") String eventID){

        return EventService.getEventAvailableSeats(eventID);

    }




}
