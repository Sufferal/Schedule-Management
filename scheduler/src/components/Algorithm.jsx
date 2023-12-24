import React from 'react'
import Step from './Step'


const Algorithm = () => {
  const steps = [
    {
      title: 'Step 1 - Preprocessing',
      description: 'Segmentation of fixed-pitch fonts is accomplished relatively simply by aligning the image to a uniform grid based on where vertical grid lines will least often intersect black areas. For proportional fonts, more sophisticated techniques are needed because whitespace between letters can sometimes be greater than that between words, and vertical lines can intersect more than one character.'
    },
    {
      title: 'Step 2 - Text Recognition',
      description: 'A technique known as iterative OCR automatically crops a document into sections based on page layout. OCR is performed on the sections individually using variable character confidence level thresholds to maximize page-level OCR accuracy. A patent from the United States Patent Office has been issued for this method'
    },
    {
      title: 'Step 3 - Postprocessing',
      description: 'OCR accuracy can be increased if the output is constrained by a lexicon – a list of words that are allowed to occur in a document. This might be, for example, all the words in the English language, or a more technical lexicon for a specific field. This technique can be problematic if the document contains words not in the lexicon, like proper nouns. Tesseract uses its dictionary to influence the character segmentation step, for improved accuracy.'
    }
  ];

  return (
   
    <div >
      <h2 className='algo-title'>Algorithm</h2>
      <p className="algo-description">
        Optical character recognition or optical character reader (OCR) is the electronic or mechanical 
        conversion of images of typed, handwritten or printed text into machine-encoded text, 
        whether from a scanned document, a photo of a document, a scene photo 
        (for example the text on signs and billboards in a landscape photo) or from subtitle text 
        superimposed on an image (for example: from a television broadcast).
      </p>
     <div className='column-container'>
     <div className='left-column'>
      {steps.map((step, index) => (<Step key={index} title={step.title}></Step>))}
     </div>
      <div className='specific-column'>
        {steps.map((step, index) => (
          <Step
            key={index}
            description={step.description}
          />
        ))}
      </div>
      </div>
    </div >

  )
}

export default Algorithm