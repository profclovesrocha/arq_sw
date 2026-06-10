package com.pay.payment_api.service;

import com.pay.payment_api.entity.Order;
import com.pay.payment_api.entity.OrderStatus;
import com.pay.payment_api.event.OrderCreatedEvent;
import com.pay.payment_api.producer.OrderEventProducer;
import com.pay.payment_api.repository.OrderRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;
import java.util.List;
import java.util.UUID;

@Service
@RequiredArgsConstructor
public class OrderService {

    private final OrderRepository orderRepository;

    private final OrderEventProducer orderEventProducer;

    public Order createOrder(Order order){

        order.setStatus(OrderStatus.PENDING);
        order.setCreatedAt(LocalDateTime.now());

        Order savedOrder = orderRepository.save(order);

        OrderCreatedEvent event = OrderCreatedEvent.builder()
                .orderId(savedOrder.getId())
                .customerId(savedOrder.getCustomerId())
                .amount(savedOrder.getAmount())
                .build();

        orderEventProducer.sendOrderCreatedEvent(event);

        return savedOrder;
    }

    public List<Order> getAllOrders(){
        return orderRepository.findAll();
    }

    public Order getOrderById(UUID id){

        return orderRepository.findById(id)
                .orElseThrow(() -> new RuntimeException("Order not found"));
    }

    public Order updateOrderStatus(UUID id, OrderStatus status){

        Order order = orderRepository.findById(id)
                .orElseThrow(() -> new RuntimeException("Order not found"));

        order.setStatus(status);

        return orderRepository.save(order);
    }
}
