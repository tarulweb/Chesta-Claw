use pyo3::prelude::*;

#[pyfunction]
fn execute_command(command: String) -> PyResult<String> {
    // In the future, this will use Docker/MicroVMs for sandboxing
    Ok(format!("Executing command: {}", command))
}

#[pymodule]
fn engine(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(execute_command, m)?)?;
    Ok(())
}
