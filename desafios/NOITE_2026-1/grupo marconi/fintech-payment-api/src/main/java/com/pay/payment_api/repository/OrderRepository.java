package com.pay.payment_api.repository;

import com.pay.payment_api.entity.Order;
import com.pay.payment_api.entity.Payment;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.UUID;

public interface OrderRepository extends JpaRepository<Order, UUID> {
}
