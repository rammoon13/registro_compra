# registro_compra/models/registro_compra.py
from odoo import models, fields, api

class RegistroCompra(models.Model):
    _name = 'registro.compra'
    _description = 'Registro de Compra'

    vendedor = fields.Many2one('hr.employee', string="Vendedor", required=True)
    empresa = fields.Many2one('res.partner', string="Empresa", required=True, domain=[('is_company', '=', True)])
    fecha_venta = fields.Date(string="Fecha de la Venta", required=True)
    linea_ids = fields.One2many('registro.compra.line', 'compra_id', string="Productos Vendidos")
    total = fields.Float(string="Total", compute="_compute_total", store=True)

    @api.depends('linea_ids.subtotal')
    def _compute_total(self):
        for record in self:
            record.total = sum(line.subtotal for line in record.linea_ids)

    @api.model
    def create(self, vals):
        """Este método se ejecuta al crear un nuevo registro de compra"""
        record = super(RegistroCompra, self).create(vals)
        return record

class RegistroCompraLine(models.Model):
    _name = 'registro.compra.line'
    _description = 'Línea de Productos en el Registro de Compra'

    compra_id = fields.Many2one('registro.compra', string="Compra", ondelete='cascade')
    producto = fields.Many2one('product.product', string="Producto", required=True)
    cantidad = fields.Integer(string="Cantidad", required=True)
    precio_unitario = fields.Float(string="Precio Unitario", related="producto.list_price", readonly=True)
    subtotal = fields.Float(string="Subtotal", compute="_compute_subtotal", store=True)

    @api.depends('cantidad', 'precio_unitario')
    def _compute_subtotal(self):
        for record in self:
            record.subtotal = record.cantidad * record.precio_unitario