package com.pay.payment_api.dto;

import jakarta.validation.constraints.NotNull;

import java.math.BigDecimal;
import java.util.UUID;

public record CreateOrderRequest(
        @NotNull
        UUID customerId,

        @NotNull
        BigDecimal amount
){}
