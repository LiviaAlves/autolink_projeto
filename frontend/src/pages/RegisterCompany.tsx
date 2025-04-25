import { useState } from 'react';
import '../styles/company.css';

const CompanyRegister = () => {
  const [formData, setFormData] = useState({
    nome_empresa: '',
    razao_social: '',
    cnpj: '',
    email: '',
    telefone: '',
    bairro: '',
    rua: '',
    cidade: '',
    estado: '',
    dono: '',
    horario_funcionamento: '',
    cpf_responsavel: '',
    rg_responsavel: '',
    conta_bancaria: '',
    imagem: null as File | null
  });

  const [previewUrl, setPreviewUrl] = useState<string | null>(null);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value, files } = e.target;
    if (name === 'imagem' && files && files[0]) {
      const file = files[0];
      setFormData((prev) => ({ ...prev, imagem: file }));
      setPreviewUrl(URL.createObjectURL(file));
    } else {
      setFormData((prev) => ({
        ...prev,
        [name]: value
      }));
    }
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    const data = new FormData();
    const enderecoCompleto = `${formData.rua}, ${formData.bairro}, ${formData.cidade} - ${formData.estado}`;

    data.append('razao_social', formData.razao_social);
    data.append('nome_fantasia', formData.nome_empresa);
    data.append('cnpj', formData.cnpj);
    data.append('telefone', formData.telefone);
    data.append('email', formData.email);
    data.append('cpf_responsavel', formData.cpf_responsavel);
    data.append('rg_responsavel', formData.rg_responsavel);
    data.append('conta_bancaria', formData.conta_bancaria);
    data.append('horario_funcionamento', formData.horario_funcionamento);
    data.append('endereco', enderecoCompleto);

    if (formData.imagem) {
      data.append('logo', formData.imagem);
    }

    try {
      const response = await fetch('http://localhost:8000/api/empresas/', {
        method: 'POST',
        body: data
      });

      if (response.ok) {
        alert('Empresa cadastrada com sucesso!');
        setFormData({
          nome_empresa: '',
          razao_social: '',
          cnpj: '',
          email: '',
          telefone: '',
          bairro: '',
          rua: '',
          cidade: '',
          estado: '',
          dono: '',
          horario_funcionamento: '',
          cpf_responsavel: '',
          rg_responsavel: '',
          conta_bancaria: '',
          imagem: null
        });
        setPreviewUrl(null);
      } else {
        const errorData = await response.json();
        console.error('Erro ao cadastrar empresa:', errorData);
        alert('Erro ao cadastrar empresa. Verifique os dados.');
      }
    } catch (error) {
      console.error('Erro na requisição:', error);
      alert('Erro de conexão ao cadastrar a empresa.');
    }
  };

  return (
    <div className="company-register-page">
      <img src="/autolink2.png" alt="Logo" className="company-register-logo" />
      <div className="company-register-container">
        <h2>Registrar Empresa</h2>
        <form className="company-register-form" onSubmit={handleSubmit}>
          <div className="company-register-row">
            <input
              type="text"
              name="nome_empresa"
              placeholder="Nome Fantasia"
              value={formData.nome_empresa}
              onChange={handleChange}
              required
            />
            <input
              type="text"
              name="razao_social"
              placeholder="Razão Social"
              value={formData.razao_social}
              onChange={handleChange}
              required
            />
          </div>

          <div className="company-register-row">
            <input
              type="text"
              name="cnpj"
              placeholder="CNPJ"
              value={formData.cnpj}
              onChange={handleChange}
              required
            />
            <input
              type="email"
              name="email"
              placeholder="Email da empresa"
              value={formData.email}
              onChange={handleChange}
              required
            />
          </div>

          <div className="company-register-row">
            <input
              type="text"
              name="telefone"
              placeholder="Telefone"
              value={formData.telefone}
              onChange={handleChange}
              required
            />
            <input
              type="text"
              name="horario_funcionamento"
              placeholder="Horário de Funcionamento (ex: 08:00 - 18:00)"
              value={formData.horario_funcionamento}
              onChange={handleChange}
              required
            />
          </div>

          <div className="company-register-row">
            <input
              type="text"
              name="cpf_responsavel"
              placeholder="CPF do Responsável"
              value={formData.cpf_responsavel}
              onChange={handleChange}
              required
            />
            <input
              type="text"
              name="rg_responsavel"
              placeholder="RG do Responsável"
              value={formData.rg_responsavel}
              onChange={handleChange}
              required
            />
          </div>

          <div className="company-register-row">
            <input
              type="text"
              name="conta_bancaria"
              placeholder="Conta Bancária"
              value={formData.conta_bancaria}
              onChange={handleChange}
              required
            />
            <input
              type="text"
              name="dono"
              placeholder="Dono"
              value={formData.dono}
              onChange={handleChange}
            />
          </div>

          <div className="company-register-row">
            <input
              type="text"
              name="bairro"
              placeholder="Bairro"
              value={formData.bairro}
              onChange={handleChange}
            />
            <input
              type="text"
              name="rua"
              placeholder="Rua"
              value={formData.rua}
              onChange={handleChange}
            />
          </div>

          <div className="company-register-row">
            <input
              type="text"
              name="cidade"
              placeholder="Cidade"
              value={formData.cidade}
              onChange={handleChange}
            />
            <input
              type="text"
              name="estado"
              placeholder="Estado"
              value={formData.estado}
              onChange={handleChange}
            />
          </div>

          <div className="company-register-row">
            <input type="file" name="imagem" accept="image/*" onChange={handleChange} />
          </div>

          {previewUrl && (
            <div style={{ textAlign: 'center', margin: '10px 0' }}>
              <p style={{ margin: '0px 0px 15px 0px' }}>Logo da empresa</p>
              <img
                src={previewUrl}
                alt="Logo"
                style={{ maxWidth: '150px', borderRadius: '8px' }}
              />
            </div>
          )}

          <button type="submit" className="company-register-submit">
            Cadastrar
          </button>
        </form>
      </div>
    </div>
  );
};

export default CompanyRegister;
