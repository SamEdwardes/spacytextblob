import React from 'react';
import clsx from 'clsx';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import useBaseUrl from '@docusaurus/useBaseUrl';
import styles from './styles.module.css';

const features = [
  {
    description: (
      <>
        <h2>
          Installation
        </h2>
        <p>
          Install spacytextblob using pip:
        </p>
        <pre>
          pip install spacytextblob
        </pre>
        Then
        <pre>
          pip install spacytextblob
        </pre>
        <h2>
          Quickstart
        </h2>
        Load the pipeline into spacy pipeline:
        <pre class="python">
          >>> import spacy <br/>
          >>> from spacytextblob.textblob import SpacyTextBlob <br/>
          >>> <br/>
          >>> nlp = spacy.load('en_core_web_sm') <br/>
          >>> spacy_text_blob = SpacyTextBlob() <br/>
          >>> nlp.add_pipe(spacy_text_blob) <br/>
          >>> <br/>
          >>> # pipeline contains component name <br/>
          >>> print(nlp.pipe_names) <br/>
          ['tagger', 'parser', 'ner', 'spaCyTextBlob'] <br/>
        </pre>
        Now you can use the spacy nlp object like normal:
        <pre class="python">
          >>> text = "I had a really horrible day. It was the worst day ever!" <br/>
          >>> doc = nlp(text) <br/>
          >>> print('Polarity:', doc._.polarity) <br/>
          Polarity: 0.55 <br/>
          >>> print('Sujectivity:', doc._.subjectivity) <br/>
          Sujectivity: 0.65 <br/>
          >>> print('Assessments:', doc._.assessments) <br/>
          Assessments: [(['wow'], 0.1, 1.0, None), (['best', '!'], 1.0, 0.3, None)] <br/>
        </pre>
      </>
    ),
  },
];


function Feature({imageUrl, title, description}) {
  const imgUrl = useBaseUrl(imageUrl);
  return (
    <div className={clsx('col col--12', styles.feature)}>
      {imgUrl && (
        <div className="text--center">
          <img className={styles.featureImage} src={imgUrl} alt={title} />
        </div>
      )}
      <h3>{title}</h3>
      <p>{description}</p>
    </div>
  );
}

function Home() {
  const context = useDocusaurusContext();
  const {siteConfig = {}} = context;
  return (
    <Layout
      title={`Hello from ${siteConfig.title}`}
      description="Description will go into a meta tag in <head />">
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
        {features && features.length > 0 && (
          <section className={styles.features}>
            <div className="container">
              <div className="row">
                {features.map((props, idx) => (
                  <Feature key={idx} {...props} />
                ))}
              </div>
            </div>
          </section>
        )}
      </main>
    </Layout>
  );
}

export default Home;
