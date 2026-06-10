package com.pay.payment_api.controller;

import com.pay.payment_api.dto.CreateOrderRequest;
import com.pay.payment_api.dto.OrderResponse;
import com.pay.payment_api.entity.Order;
import com.pay.payment_api.entity.OrderStatus;
import com.pay.payment_api.mapper.OrderMapper;
import com.pay.payment_api.service.OrderService;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.responses.ApiResponse;
import io.swagger.v3.oas.annotations.responses.ApiResponses;
import io.swagger.v3.oas.annotations.tags.Tag;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.UUID;

@RestController
@RequestMapping("/orders")
@RequiredArgsConstructor
@Tag(name = "orders", description = "API de gerenciamento de pedidos")
public class OrderController {

    private final OrderService orderService;

    // Create Order
    @PostMapping
    @Operation(summary = "Criar pedido", description = "Cria um novo pedido e envia evento para o RabbitMQ")
    @ApiResponses(value = {
            @ApiResponse(responseCode = "201", description = "Pedido criado com sucesso"),
            @ApiResponse(responseCode = "400", description = "Dados inválidos"),
            @ApiResponse(responseCode = "500", description = "Erro interno do servidor")
    })
    public ResponseEntity<OrderResponse> createOrder(@RequestBody CreateOrderRequest request){

        Order order = OrderMapper.toEntity(request);

        Order createdOrder = orderService.createOrder(order);

        OrderResponse response = OrderMapper.toResponse(createdOrder);

        return ResponseEntity.status(HttpStatus.CREATED).body(response);
    }

    // Get All Orders
    @GetMapping
    @Operation(summary = "Listar pedidos", description = "Retorna todos os pedidos cadastrados")
    @ApiResponses(value = {
            @ApiResponse(responseCode = "200", description = "Lista retornada com sucesso"),
            @ApiResponse(responseCode = "500", description = "Erro interno do servidor")
    })
    public ResponseEntity<List<OrderResponse>> getAllOrders(){

        List<Order> orders = orderService.getAllOrders();

        List<OrderResponse> response = orders.stream()
                .map(OrderMapper::toResponse)
                .toList();

        return ResponseEntity.ok(response);
    }
    @GetMapping("/{id}")
    @Operation(summary = "Buscar pedido por ID", description = "Retorna um pedido específico pelo seu ID")
    @ApiResponses(value = {
            @ApiResponse(responseCode = "200", description = "Pedido encontrado"),
            @ApiResponse(responseCode = "404", description = "Pedido não encontrado")
    })
    public ResponseEntity<OrderResponse> getOrderById(@PathVariable UUID id){

        Order order = orderService.getOrderById(id);

        OrderResponse response = OrderMapper.toResponse(order);

        return ResponseEntity.ok(response);
    }
    @PatchMapping("/{id}/status")
    @Operation(
            summary = "Atualizar status do pedido",
            description = "Atualiza o status de um pedido existente"
    )
    @ApiResponses(value = {
            @ApiResponse(responseCode = "200", description = "Status atualizado com sucesso"),
            @ApiResponse(responseCode = "404", description = "Pedido não encontrado"),
            @ApiResponse(responseCode = "400", description = "Status inválido")
    })
    public ResponseEntity<OrderResponse> updateOrderStatus(
            @PathVariable UUID id,
            @RequestParam OrderStatus status){

        Order order = orderService.updateOrderStatus(id, status);

        OrderResponse response = OrderMapper.toResponse(order);

        return ResponseEntity.ok(response);
    }
}