#[cfg(test)]
mod tests{
    use streamtracer::interp;
    use ndarray::{array};

    #[test]
    fn test_interp_trilin() {
        let values = array![[[0., 1.], [0., 1.]],
                            [[0., 1.], [0., 1.]]];
        let a = array![0.3, 0.2, 0.4];
        let b = interp::interp_trilinear(&values, &a);
        assert_eq!(b, 0.4);
    }
}