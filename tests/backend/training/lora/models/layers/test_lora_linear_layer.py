import pytest
import torch

from invokeai.backend.training.lora.models.layers import LoRALinearLayer


def test_lora_linear_layer_output_dim():
    """Test LoRALinearLayer produces an output with the expected dimension."""
    batch_size = 10
    in_features = 8
    out_features = 16
    layer = LoRALinearLayer(in_features, out_features, 2)

    x = torch.rand((batch_size, in_features))
    with torch.no_grad():
        y = layer.forward(x)

    assert y.shape == (batch_size, out_features)


def test_lora_linear_layer_invalid_input_dim():
    """Test that LoRALinearLayer throws an exception if it receives an input with invalid dimensions."""
    in_features = 8
    out_features = 16
    layer = LoRALinearLayer(in_features, out_features, 2)

    x = torch.rand((10, in_features + 1))  # Bad input dimension.

    with pytest.raises(RuntimeError):
        _ = layer.forward(x)


def test_lora_linear_layer_zero_after_init():
    """Test that a newly-initialized LoRALinearLayer produces all zeros before it is trained."""
    batch_size = 10
    in_features = 8
    out_features = 16
    layer = LoRALinearLayer(in_features, out_features, 2)

    x = torch.rand((batch_size, in_features))
    with torch.no_grad():
        y = layer.forward(x)

    assert not torch.allclose(x, torch.Tensor([0.0]), rtol=0.0)  # The random input was non-zero.
    assert torch.allclose(y, torch.Tensor([0.0]), rtol=0.0)  # The untrained outputs are zero.