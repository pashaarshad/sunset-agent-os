from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
import os
try:
    from PIL import Image
    from io import BytesIO
except ImportError:
    pass

def add_safe_picture(doc, path, width):
    try:
        if os.path.exists(path):
            img = Image.open(path).convert('RGB')
            stream = BytesIO()
            img.save(stream, format='PNG')
            stream.seek(0)
            doc.add_picture(stream, width=width)
            return True
    except Exception as e:
        print(f"Skipping image {path} due to error: {e}")
    return False

def create_paper():
    doc = Document()
    
    # Title
    title = doc.add_heading('Sunset Agent OS: A Paradigm-Shifting AI-Driven Operating System Architecture', 0)
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    # Authors
    authors = doc.add_paragraph()
    authors.alignment = WD_ALIGN_PARAGRAPH.CENTER
    authors.add_run('Arshad Pasha\n').bold = True
    authors.add_run('Arun\n').bold = True
    authors.add_run('Lead Architects & Researchers\n')
    
    # Header Image
    add_safe_picture(doc, 'images/sunset_os_background.png', Inches(6.0))

    # Abstract
    doc.add_heading('Abstract', level=1)
    doc.add_paragraph('Sunset Agent OS redefines the traditional relationship between hardware, operating systems, and users. By integrating an intelligent AI Agent at the core level rather than as a secondary application, the system transitions from a passive tool to a proactive intelligence. This paper explores the dual-partition architecture that segregates standard user environments from an isolated AI controller, ensuring security, privacy, and unprecedented resource optimization.')

    # Introduction
    doc.add_heading('1. Introduction', level=1)
    doc.add_paragraph('Modern operating systems are built on rigid scheduling routines that often require human intervention for complex resource management. Sunset Agent OS shifts this logic by building a bridge between traditional OS kernels and a dedicated AI partition. The vision is to create an OS that understands user behavior and autonomously manages memory, CPU cycles, and system health.')

    # Core Concept
    doc.add_heading('2. The Dual-Partition Architecture', level=1)
    doc.add_paragraph('The fundamental innovation of Sunset Agent OS is its Dual Partition System:')
    
    doc.add_heading('2.1 Normal OS Partition (User Environment)', level=2)
    doc.add_paragraph('This partition provides a familiar environment for standard applications like browsers and IDEs, running similarly to Windows or Linux.')
    
    doc.add_heading('2.2 AI Agent Partition (Intelligent Controller)', level=2)
    doc.add_paragraph('An isolated, dedicated partition controlled exclusively by the AI. It cannot be terminated by user-side processes and holds its own system resources for secure, local analysis.')
    
    if add_safe_picture(doc, 'architecture/dual_partition_diagram.png', Inches(5.0)):
        p_img = doc.add_paragraph('Figure 1: Dual Partition Architecture Diagram')
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER

    # Architecture
    doc.add_heading('3. System Architecture and Flow', level=1)
    doc.add_paragraph('The AI Agent acts as a background service controlling applications through a secure Control Bridge API. This ensures that while the AI has administrative oversight, user applications cannot hijack its privileges.')
    
    if add_safe_picture(doc, 'architecture/new_system_architecture.png', Inches(5.0)):
        p_img2 = doc.add_paragraph('Figure 2: Modern System Architecture')
        p_img2.alignment = WD_ALIGN_PARAGRAPH.CENTER

    # Implementation Strategy (Step-by-Step)
    doc.add_heading('4. Implementation Strategy (Step-by-Step)', level=1)
    doc.add_paragraph('The development of Sunset Agent OS follows a structured roadmap to ensure stability and efficiency:')
    
    steps = [
        ("Step 1: AI System Controller Prototype", "Develop a Python-based background service using libraries like psutil to monitor system health and process life-cycles."),
        ("Step 2: Dual Partition Isolation", "Establish a secure communication bridge between the standard OS environment and the isolated AI domain."),
        ("Step 3: Intelligent Memory Allocation", "Implement dynamic RAM allocation logic that saves states and suspends background tasks based on real-time priority."),
        ("Step 4: Modular LLM Integration", "Design a flexible 'Brain' interface that allows the system to swap or update underlying Large Language Models (LLMs) without breaking the OS core."),
        ("Step 5: Privacy-First Analytics", "Deploy local behavior analysis algorithms to ensure user data never leaves the device while the AI learns usage patterns."),
        ("Step 6: Performance Optimization Layers", "Integrate specific boosters for development (Dev Assistant) and Gaming profiles (Gaming Booster).")
    ]
    
    for title, desc in steps:
        p = doc.add_paragraph(style='List Bullet')
        p.add_run(f"{title}: ").bold = True
        p.add_run(desc)

    # Future Vision
    doc.add_heading('5. Future Vision and Applications', level=1)
    doc.add_paragraph('Beyond simple optimization, Sunset Agent OS aims to be a complete assistant that auto-configures dev environments, manages privacy with hardware-level blocks, and serves as a local-first hybrid AI platform.')
    
    add_safe_picture(doc, 'images/future_vision.png', Inches(5.0))

    # Conclusion
    doc.add_heading('Conclusion', level=1)
    doc.add_paragraph('Sunset Agent OS represents a major leap in personal computing. By decentralizing the AI partition and granting it proactive control, we eliminate the bottlenecks of traditional OS designs. The result is a smarter, faster, and more secure computing experience.')

    # Save
    save_path = 'Sunset_Agent_OS_Technical_Paper.docx'
    doc.save(save_path)
    print(f"Paper generated successfully: {save_path}")

if __name__ == '__main__':
    create_paper()
