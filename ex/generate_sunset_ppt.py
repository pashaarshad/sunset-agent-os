from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
import os
try:
    from PIL import Image
    import io
except ImportError:
    pass

def add_image_safe(slide, image_path, left, top, width=None, height=None):
    if not os.path.exists(image_path):
        return False
    try:
        img = Image.open(image_path).convert('RGB')
        stream = io.BytesIO()
        img.save(stream, format='PNG')
        stream.seek(0)
        slide.shapes.add_picture(stream, left, top, width=width, height=height)
        return True
    except Exception as e:
        print(f"Skipping {image_path}: {e}")
        return False

def create_ppt():
    prs = Presentation()
    
    # Title Slide
    slide = prs.slides.add_slide(prs.slide_layouts[0])
    title = slide.shapes.title
    subtitle = slide.placeholders[1]
    
    title.text = "Sunset Agent OS"
    subtitle.text = "A Paradigm-Shifting AI-Driven Operating System\n\nBy: Arshad Pasha & Arun"
    
    # Background Image on Title
    add_image_safe(slide, "images/sunset_os_background.png", Inches(0.5), Inches(4.5), height=Inches(2.5))

    # 1. Vision
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    slide.shapes.title.text = "The Vision"
    tf = slide.placeholders[1].text_frame
    tf.text = "Shift the traditional OS logic from static to intelligent."
    p = tf.add_paragraph()
    p.text = "Build a bridge between traditional Kernels and an AI Partition."
    p = tf.add_paragraph()
    p.text = "Proactive Management vs. Passive Tools."

    # 2. The Problem
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    slide.shapes.title.text = "The Problem: Traditional OS Limits"
    tf = slide.placeholders[1].text_frame
    tf.text = "- Rigid scheduling routines."
    p = tf.add_paragraph()
    p.text = "- Manual memory management (closing apps)."
    p = tf.add_paragraph()
    p.text = "- Lack of context-aware performance boosting."
    p = tf.add_paragraph()
    p.text = "- Privacy data forced to cloud for processing."

    # 3. Core Concept: Dual Partition
    slide = prs.slides.add_slide(prs.slide_layouts[5])
    slide.shapes.title.text = "Core Concept: Dual Partition System"
    add_image_safe(slide, "architecture/dual_partition_diagram.png", Inches(1.5), Inches(1.5), height=Inches(5))

    # 4. Partition Details
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    slide.shapes.title.text = "1. Normal OS vs. 2. AI Agent"
    tf = slide.placeholders[1].text_frame
    tf.text = "Normal OS Partition:"
    p = tf.add_paragraph()
    p.text = "- Standard Apps (Browsers, IDEs, Games)."
    p = tf.add_paragraph()
    p.text = "- Familiar User Environment."
    p = tf.add_paragraph()
    p.text = "\nAI Agent Partition:"
    p = tf.add_paragraph()
    p.text = "- Isolated, Secure Controller."
    p = tf.add_paragraph()
    p.text = "- Cannot be terminated by user-side processes."

    # 5. System Architecture
    slide = prs.slides.add_slide(prs.slide_layouts[5])
    slide.shapes.title.text = "Modern System Architecture"
    add_image_safe(slide, "architecture/new_system_architecture.png", Inches(1), Inches(1.5), width=Inches(8))

    # 6. Step-by-Step Implementation
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    slide.shapes.title.text = "Step-by-Step Roadmap"
    tf = slide.placeholders[1].text_frame
    tf.text = "1. Prototype: Python + psutil for system health."
    p = tf.add_paragraph()
    p.text = "2. Isolation: Establish the Secure Control Bridge."
    p = tf.add_paragraph()
    p.text = "3. Memory: Dynamic RAM optimization logic."
    p = tf.add_paragraph()
    p.text = "4. LLM: Modular brain switching (Local First)."
    p = tf.add_paragraph()
    p.text = "5. Booster: Specific game & dev profile triggers."

    # 7. AI Agent Flow
    slide = prs.slides.add_slide(prs.slide_layouts[5])
    slide.shapes.title.text = "AI Agent Logic Flow"
    add_image_safe(slide, "images/ai_agent_flow.png", Inches(1), Inches(1.5), width=Inches(8))

    # 8. Future Vision
    slide = prs.slides.add_slide(prs.slide_layouts[5])
    slide.shapes.title.text = "Futuristic Control Concept"
    add_image_safe(slide, "images/future_vision.png", Inches(2), Inches(1.5), height=Inches(5))

    # 9. Conclusion
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    slide.shapes.title.text = "Conclusion"
    tf = slide.placeholders[1].text_frame
    tf.text = "Sunset Agent OS is not just an OS—it's a proactive intelligence."
    p = tf.add_paragraph()
    p.text = "Privacy-first, AI-driven, and highly optimized."
    p = tf.add_paragraph()
    p.text = "The future of autonomous computing."

    # Save
    save_path = 'Sunset_Agent_OS_Presentation.pptx'
    prs.save(save_path)
    print(f"Presentation generated successfully: {save_path}")

if __name__ == '__main__':
    create_ppt()
