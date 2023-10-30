import React, { useState, useEffect, useRef } from "react";

function ImageGallery({ images }) {
    // 로드된 이미지의 상태를 저장하는 state
    const [loadedImages, setLoadedImages] = useState([]);

    // 각 이미지에 대한 참조를 저장하는 ref
    const imageRefs = useRef([]);

    useEffect(() => {
        // Intersection Observer를 사용하여 이미지가 뷰포트에 나타날 때 로드되도록 합니다.
        const observer = new IntersectionObserver(
            (entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        const lazyImage = entry.target;
                        lazyImage.src = lazyImage.dataset.src; // 실제 이미지 경로로 src를 설정
                        setLoadedImages(prev => [...prev, lazyImage.dataset.src]);
                        observer.unobserve(lazyImage); // 이미지가 로드되면 관찰을 중단
                    }
                });
            },
            {
                rootMargin: "100px 0px" // 추가적인 여백을 설정하여 이미지를 미리 로드
            }
        );

        imageRefs.current.forEach(img => observer.observe(img)); // 각 이미지를 관찰 시작

        return () => {
            imageRefs.current.forEach(img => observer.unobserve(img)); // 컴포넌트가 언마운트될 때 관찰 중단
        };
    }, [images]);

    return (
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '10px' }}>
            {images.map((img, index) => (
                <img
                    key={index}
                    ref={el => imageRefs.current[index] = el}
                    data-src={img}
                    alt=""
                    style={{ 
                        width: '200px',  // 이미지의 너비 설정
                        height: '200px', // 이미지의 높이 설정
                        background: loadedImages.includes(img) ? 'transparent' : '#e0e0e0' // 로드되지 않은 이미지는 회색으로 표시
                    }}
                />
            ))}
        </div>
    );
}

export default ImageGallery;
