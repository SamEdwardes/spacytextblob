import React from 'react';
import clsx from 'clsx';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import useBaseUrl from '@docusaurus/useBaseUrl';
import styles from './styles.module.css';


const codeContent = {
  installationPip: `
  pip install spacytextblob                                                     
  `,
  installationTextBlob: `
  python -m textblob.download_corpora
  `,
  installationSpacy: `
  python -m spacy download en_core_web_sm
  `,
  quickstartImport: `
  >>> import spacy
  >>> from spacytextblob.textblob import SpacyTextBlob
  >>>
  >>> nlp = spacy.load('en_core_web_sm')
  >>> spacy_text_blob = SpacyTextBlob()
  >>> nlp.add_pipe(spacy_text_blob)
  >>>
  >>> # pipeline contains component name
  >>> print(nlp.pipe_names)
  ['tagger', 'parser', 'ner', 'spaCyTextBlob']
  `,
  quickstartNLP:`
  >>> text = "I had a really horrible day. It was the worst day ever!" 
  >>> doc = nlp(text) 
  >>> print('Polarity:', doc._.polarity) 
  Polarity: 0.55 
  >>> print('Sujectivity:', doc._.subjectivity) 
  Sujectivity: 0.65 
  >>> print('Assessments:', doc._.assessments) 
  Assessments: [(['wow'], 0.1, 1.0, None), (['best', '!'], 1.0, 0.3, None)]     
  `
}


function Home() {
  const context = useDocusaurusContext();
  const {siteConfig = {}} = context;
  return (
    <Layout
      title={`Home`}
      description="Easy sentiment analysis for spaCy using TextBlob">
      <header className={clsx('hero hero--primary', styles.heroBanner)}>
        <div className="container">
          <h1 className="hero__title">{siteConfig.title}</h1>
          <p className="hero__subtitle">{siteConfig.tagline}</p>
          <div className={styles.buttons}>
            <Link
              className={clsx(
                'button button--outline button--secondary button--lg',
                styles.getStarted,
              )}
              to={useBaseUrl('docs/')}>
              Get Started
            </Link>
          </div>
        </div>
      </header>
      <main>
        <section className={styles.features}>
          <div className="container">
            <div className="container">
              <h2>Installation</h2>
              <p>First install spacytextblob from PyPi</p>
              <pre>{codeContent.installationPip}</pre>
              <p>TextBlob requires some data to be downloaded before getting started.</p>
              <pre>{codeContent.installationTextBlob}</pre>
              <p>spaCy requires that you download a model to get started.</p>
              <pre>{codeContent.installationSpacy}</pre>
            </div>
            <div className="container">
              <h2>Quick start</h2>
              <p>First add spaCyTextBlob to the spaCy pipeline</p>
              <pre><code class="python">{codeContent.quickstartImport}</code></pre>
              <p>Then run text through the nlp pipeline as you normally would</p>
              <pre>{codeContent.quickstartNLP}</pre>
            </div>
          </div>
        </section>
      </main>
    </Layout>
  );
}

export default Home;
